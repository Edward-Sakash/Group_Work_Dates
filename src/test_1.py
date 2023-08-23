import unittest
from task_1_birthdate_weekday import get_weekday


class TestWeekday(unittest.TestCase):
    def setUp(self):
        self.date_list = [
            ("2018-08-13", "Monday"),
            ("1965-3-11", "Thursday"),
            ("1948-10-19", "Tuesday"),
            ("1952-6-3", "Tuesday"),
            ("1999-12-25", "Saturday"),
            ("1921-8-10", "Wednesday"),
            ("1949-1-12", "Wednesday"),
            ("2012-7-17", "Tuesday")
        ]
    
    def test_dates(self):
        for date in self.date_list:
            with self.subTest(msg=date[0]):
                self.assertTrue(get_weekday(date[0]) == date[1], date[0] + ":" + date[1])

if __name__ == '__main__':
    unittest.main()
