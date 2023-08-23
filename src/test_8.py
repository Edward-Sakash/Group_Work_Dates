import unittest
from task_8_calendar_birth_month import month_calendar


class TestWeekday(unittest.TestCase):
    def setUp(self):
        self.date_list = [
            ("2004-3-10", "     March 2004\
Mo Tu We Th Fr Sa Su\
 1  2  3  4  5  6  7\
 8  9 10 11 12 13 14\
15 16 17 18 19 20 21\
22 23 24 25 26 27 28\
29 30 31\
"),
            ("1907-3-29", "     March 1907\
Mo Tu We Th Fr Sa Su\
             1  2  3\
 4  5  6  7  8  9 10\
11 12 13 14 15 16 17\
18 19 20 21 22 23 24\
25 26 27 28 29 30 31\
"),
            ("1906-7-2", "     July 1906\
Mo Tu We Th Fr Sa Su\
                   1\
 2  3  4  5  6  7  8\
 9 10 11 12 13 14 15\
16 17 18 19 20 21 22\
23 24 25 26 27 28 29\
30 31\
"),
            ("1979-9-20", "   September 1979\
Mo Tu We Th Fr Sa Su\
                1  2\
 3  4  5  6  7  8  9\
10 11 12 13 14 15 16\
17 18 19 20 21 22 23\
24 25 26 27 28 29 30\
"),
            ("2013-4-14", "     April 2013\
Mo Tu We Th Fr Sa Su\
 1  2  3  4  5  6  7\
 8  9 10 11 12 13 14\
15 16 17 18 19 20 21\
22 23 24 25 26 27 28\
29 30\
"),
            ("2009-11-15", "   November 2009\
Mo Tu We Th Fr Sa Su\
                   1\
 2  3  4  5  6  7  8\
 9 10 11 12 13 14 15\
16 17 18 19 20 21 22\
23 24 25 26 27 28 29\
30\
"),
            ("1998-6-12", "     June 1998\
Mo Tu We Th Fr Sa Su\
 1  2  3  4  5  6  7\
 8  9 10 11 12 13 14\
15 16 17 18 19 20 21\
22 23 24 25 26 27 28\
29 30\
"),
            ("1996-7-31", "     July 1996\
Mo Tu We Th Fr Sa Su\
 1  2  3  4  5  6  7\
 8  9 10 11 12 13 14\
15 16 17 18 19 20 21\
22 23 24 25 26 27 28\
29 30 31\
"),
            ("1930-12-11", "   December 1930\
Mo Tu We Th Fr Sa Su\
 1  2  3  4  5  6  7\
 8  9 10 11 12 13 14\
15 16 17 18 19 20 21\
22 23 24 25 26 27 28\
29 30 31\
"),
            ("1998-5-21", "      May 1998\
Mo Tu We Th Fr Sa Su\
             1  2  3\
 4  5  6  7  8  9 10\
11 12 13 14 15 16 17\
18 19 20 21 22 23 24\
25 26 27 28 29 30 31\
"),
        ]

    def test_dates(self):
        for date in self.date_list:
            with self.subTest(msg=date[0]):
                self.assertTrue(month_calendar(date[0]).replace("\n", "") == date[1], date[0] + ":" + date[1])


if __name__ == '__main__':
    unittest.main()

