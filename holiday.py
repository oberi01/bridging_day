from typing import Dict
import argparse
import requests
import datetime

DAY_OF_WEEK = {
    "MONTAG": 0,
    "DIENSTAG": 1,
    "MITTWOCH": 2,
    "DONNERSTAG": 3,
    "FREITAG": 4,
    "SAMSTAG": 5,
    "SONNTAG": 6
}
INV_DOW = {v: k for k, v in DAY_OF_WEEK.items()}
STATES = ['bw', 'by', 'be', 'bb', 'hb', 'hh', 'he', 'mv',
          'ni', 'nw', 'rp', 'sl', 'sn', 'st', 'sh', 'th']
URI_FT_SERVER = "https://get.api-feiertage.de"


def string_to_date(dt, d_format='%Y-%m-%d'):
    return datetime.datetime.strptime(dt, d_format)


def date_to_string(date, d_format='%Y-%m-%d'):
    return datetime.datetime.strftime(date, d_format)


def day_of_week(dt):
    return string_to_date(dt).weekday()


def get_holiday(year: int, state: str = "by") -> Dict:
    """ Get German holidays for given year and state.
    :return:  dict e.g. {'Neujahr': '2022-01-01', ...}
              in case of Error raises RuntimeError
    """
    result = requests.get(f"{URI_FT_SERVER}?years={year}&states={state}")
    if not result.ok:
        # it appears this WS is always returning ok, this code is probably never reached
        raise RuntimeError("Web service error behaviour has changed")
    content = result.json()

    # error is inside content ...
    if 'status' in content and content['status'] == 'error':
        raise RuntimeError(content['error_description'])

    # transform into a more suitable format
    f_dict = {x['fname']: x['date'] for x in content['feiertage']}
    return f_dict


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-y", "--year", required=True, help="Jahr für das Brückentage ermittelt werden sollen.")
    parser.add_argument("-s", "--state", required=True,
                        help=f"Bundesland zur Ermittlung der Urlaubstage. Kürzel={STATES}")
    args = parser.parse_args()
    assert args.state in STATES, f"Unbekanntes Bundesland: {args.state}; erwartet: {STATES}"

    for h_name, h_date in get_holiday(args.year).items():
        if day_of_week(h_date) == DAY_OF_WEEK['DIENSTAG']:   # yesterday, i.e. delta=-1d
            delta = datetime.timedelta(days=-1)
        elif day_of_week(h_date) == DAY_OF_WEEK['DONNERSTAG']:
            delta = datetime.timedelta(days=1)              # tomorrow, i.e. delta=1d
        else:
            continue

        b_day = date_to_string(string_to_date(h_date) + delta)
        print(f'Brückentag zu {h_name} am {h_date} ist am {b_day}, ein {INV_DOW[day_of_week(b_day)]}.')
