import unittest
import datetime
import calendar
from task_3_birthday_weekday import get_weekday


class TestWeekday(unittest.TestCase):
    def setUp(self):
        this_year = datetime.datetime.today().year
        self.date_list = [
            ("2018-08-13", calendar.day_name[datetime.datetime(year=this_year, month=8, day=13).weekday()]),
            ("1965-3-11", calendar.day_name[datetime.datetime(year=this_year, month=3, day=11).weekday()]),
            ("1948-10-19", calendar.day_name[datetime.datetime(year=this_year, month=10, day=19).weekday()]),
            ("1952-6-3", calendar.day_name[datetime.datetime(year=this_year, month=6, day=3).weekday()]),
            ("1999-12-25", calendar.day_name[datetime.datetime(year=this_year, month=12, day=25).weekday()]),
            ("1921-8-10", calendar.day_name[datetime.datetime(year=this_year, month=8, day=10).weekday()]),
            ("1949-1-12", calendar.day_name[datetime.datetime(year=this_year, month=1, day=12).weekday()]),
            ("2012-7-17", calendar.day_name[datetime.datetime(year=this_year, month=7, day=17).weekday()]),
        ]

    def test_dates(self):
        for date in self.date_list:
            with self.subTest(msg=date[0]):
                self.assertTrue(get_weekday(date[0]) == date[1], f"Birthdate: {date[0]}  - Birthday this year : {date[1]}")


if __name__ == '__main__':
    unittest.main()
