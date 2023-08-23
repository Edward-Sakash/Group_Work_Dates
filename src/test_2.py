import unittest
from task_2_day_number_birthday import day_num_in_year
import calendar
import datetime

# Do not modify the following
# Test Class : code for running the test
class TestDayNumGetter(unittest.TestCase):
    def setUp(self):
        add_leap = 0
        if calendar.isleap(datetime.datetime.today().year):
            add_leap = 1
        self.days = [
            ('1922-4-29', 119 + add_leap, f"The function should return {119 + add_leap}"),
            ('2011-10-03', 276 + add_leap, f"The function should return {276 + add_leap}"),
            ('2004-2-22', 53 + add_leap, f"The function should return {53 + add_leap}"),
            ('2008-3-1', 60 + add_leap, f"The function should return {60 + add_leap}"),
            ('2008-1-15', 15 + add_leap, f"The function should return {60 + add_leap}"),
        ]

    def test_DayNum(self):
        for day in self.days:
            with self.subTest(msg=day[0]):
                self.assertTrue(day_num_in_year(day[0]) == day[1], day[2])


if __name__ == '__main__':
    unittest.main()
