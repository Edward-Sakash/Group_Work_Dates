import unittest
from task_7_week_number_birthdate import week_number


# Do not modify the following
# Test Class : code for running the test
class TestWeekNumGetter(unittest.TestCase):
    def setUp(self):
        self.week_num_list = [
            (("04/10/2001", "%d/%m/%Y"), 40, "The function should return 40"),
            (("14.03.2004", "%d.%m.%Y"), 11, "The function should return 10"),
            (("01.01.1987", "%d.%m.%Y"), 1, "The function should return 1")
        ]

    def test_weeks(self):
        for day in self.week_num_list:
            with self.subTest(msg=day[0][0]):
                self.assertTrue(week_number(day[0][0], day[0][1]) == day[1], day[2])


if __name__ == '__main__':
    unittest.main()
