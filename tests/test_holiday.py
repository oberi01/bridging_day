from unittest import TestCase
from holiday import get_holiday, DAY_OF_WEEK, day_of_week


class Test(TestCase):
    def test_get_holiday(self):
        f = get_holiday(2022, "by")
        assert f['Neujahr'] == '2022-01-01'

    def test_get_holiday_neg(self):
        with self.assertRaises(RuntimeError):
            get_holiday(2022, "aa")

    def test_day_of_week(self):
        assert day_of_week('2022-08-14') == DAY_OF_WEEK['SONNTAG']
