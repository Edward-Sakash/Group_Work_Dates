import unittest
from task_4_day_number_birthdate import day_num_in_year


# Do not modify the following
# Test Class : code for running the test
class TestDayNumGetter(unittest.TestCase):
    def setUp(self):
        self.days = [
            ('1922-4-29', 119, "The function should return 119"),
            ('2011-10-03', 276, f"The function should return 276"),
            ('2004-2-22', 53, f"The function should return 53"),
            ('2008-3-1', 60, f"The function should return 60"),
            ('2008-1-15', 15, f"The function should return 60"),
        ]

    def test_DayNum(self):
        for day in self.days:
            with self.subTest(msg=day[0]):
                self.assertTrue(day_num_in_year(day[0]) == day[1], day[2])


if __name__ == '__main__':
    unittest.main()
