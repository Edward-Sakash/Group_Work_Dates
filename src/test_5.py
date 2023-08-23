import unittest
from task_5_day_difference import get_birthday_difference


class TestWeekday(unittest.TestCase):
    def setUp(self):
        self.date_list = [
            ("1912-9-1", "1974-12-31", "22766"),
            ("1956-4-15", "1930-7-18", "9403"),
            ("2019-1-8", "1991-6-4", "10080"),
            ("1968-7-10", "1952-7-23", "5831"),
            ("1940-2-20", "1906-5-21", "12328"),
            ("1968-11-10", "1921-9-3", "17235"),
            ("2013-9-19", "1982-9-15", "11327"),
            ("1997-2-19", "2002-2-20", "1827"),
            ("1994-6-8", "1925-10-30", "25058"),
            ("2005-12-2", "2005-12-1", "1"),
        ]

    def test_dates(self):
        for date in self.date_list:
            with self.subTest(msg=date[0]):
                self.assertTrue(str(get_birthday_difference(date[0], date[1])) == date[2],
                                f"The function must return {date[2]}")


if __name__ == '__main__':
    unittest.main()
