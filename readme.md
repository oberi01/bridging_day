# Purpose
This little project shows the computation of bridging days for Germany,
i.e. days before a holiday on Tuesday or after a holiday on 
Thursday.
Inspired by an CT [article](https://ct.de/yk5u) which describes a 
"cumbersome method" using Excel (quote from article).

# Functionality
The holiday data is fetched from a Webservice.
The computed bridging days are printed in German language to stdout.

# Usage
The Python script allows to specify the year and German state for 
which the bridging days shall be computed.

    python holiday.py --help
    usage: holiday.py [-h] -y YEAR -s STATE
    
    optional arguments:
    -h, --help            show this help message and exit
    -y YEAR, --year YEAR  Jahr für das Brückentage ermittelt werden sollen.
    -s STATE, --state STATE
    Bundesland zur Ermittlung der Urlaubstage.
    Kürzel=['bw', 'by', 'be', 'bb', 'hb', 'hh', 'he',
    'mv', 'ni', 'nw', 'rp', 'sl', 'sn', 'st', 'sh', 'th']

# Example Output
    python holiday.py -y 2022 -s by
    Brückentag zu Christi Himmelfahrt am 2023-05-18 ist am 2023-05-19, ein FREITAG.
    Brückentag zu Fronleichnam am 2023-06-08 ist am 2023-06-09, ein FREITAG.
    Brückentag zu Augsburger Friedensfest am 2023-08-08 ist am 2023-08-07, ein MONTAG.
    Brückentag zu Mariä Himmelfahrt am 2023-08-15 ist am 2023-08-14, ein MONTAG.
    Brückentag zu Tag der deutschen Einheit am 2023-10-03 ist am 2023-10-02, ein MONTAG.
    Brückentag zu 2. Weihnachtstag am 2023-12-26 ist am 2023-12-25, ein MONTAG.