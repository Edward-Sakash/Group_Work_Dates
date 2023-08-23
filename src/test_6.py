import unittest
import datetime
from task_6_number_sundays import total_sunday_counts


# Do not modify the following
# Test Class : code for running the test
class TestDaysCounter(unittest.TestCase):
    @staticmethod
    def helper(date_string):
        count = 0
        birthdate = datetime.datetime.strptime(date_string, "%Y-%m-%d")
        for i in range(1 + (datetime.datetime.today() - birthdate).days):
            test_day = birthdate + datetime.timedelta(days=i)
            if test_day.weekday() == 6:
                count += 1
        return count

    def setUp(self):
        self.res = [
            TestDaysCounter.helper("1988-1-25"),
            TestDaysCounter.helper("1989-12-6"),
            TestDaysCounter.helper("2004-12-13"),
            TestDaysCounter.helper("2020-3-6"),
        ]
        self.days = [
            ("1988-1-25", self.res[0], f"The function should return {self.res[0]}"),
            ("1989-12-6", self.res[1], f"The function should return {self.res[1]}"),
            ("2004-12-13", self.res[2], f"The function should return {self.res[2]}"),
            ("2020-3-6", self.res[3], f"The function should return {self.res[3]}")
        ]

    def test_days_counter(self):
        for day in self.days:
            with self.subTest(msg=day[0]):
                self.assertTrue(total_sunday_counts(day[0]) == day[1], day[2])


if __name__ == '__main__':
    unittest.main()
