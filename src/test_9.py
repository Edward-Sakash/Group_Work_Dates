import unittest
import datetime
from task_9_days_till_next_birthday import number_days


# Do not modify the following
# Test Class : code for running the test
class TestNumberDays(unittest.TestCase):
    @staticmethod
    def helper(date_str, date_for):
        birthdate_obj = datetime.datetime.strptime(date_str, date_for)
        this_year = datetime.date.today().year
        birthday_obj = datetime.date(year=this_year, month=birthdate_obj.month, day=birthdate_obj.day)
        today_obj = datetime.date.today()

        if birthday_obj <= today_obj:
            birthday_obj = datetime.date(year=this_year + 1, month=birthdate_obj.month, day=birthdate_obj.day)

        return (birthday_obj - today_obj).days

    def setUp(self):
        self.dates = [
            [("04/10/2001", "%d/%m/%Y"), TestNumberDays.helper("04/10/2001", "%d/%m/%Y")],
            [("14.03.2004", "%d.%m.%Y"), TestNumberDays.helper("14.03.2004", "%d.%m.%Y")],
            [("01.01.1987", "%d.%m.%Y"), TestNumberDays.helper("01.01.1987", "%d.%m.%Y")],
            [("11.10.1979", "%d.%m.%Y"), TestNumberDays.helper("11.10.1979", "%d.%m.%Y")],
            [("2010-12-31", "%Y-%m-%d"), TestNumberDays.helper("2010-12-31", "%Y-%m-%d")],
        ]
        self.week_num_list = [
            (self.dates[i][0], self.dates[i][1], f"The function should return {self.dates[i][1]}")
            for i in range (len(self.dates))
        ]

    def test_weeks(self):
        for day in self.week_num_list:
            with self.subTest(msg=day[0][0]):
                self.assertTrue(number_days(day[0][0], day[0][1]) == day[1], day[2])


if __name__ == '__main__':
    unittest.main()
