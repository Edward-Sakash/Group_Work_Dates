from task_0 import get_birthday
from task_1_birthdate_weekday import get_weekday as gw1
from task_2_day_number_birthday import day_num_in_year
from task_3_birthday_weekday import get_weekday as gw2
from task_4_day_number_birthdate import day_num_in_year as dn1
from task_5_day_difference import get_birthday_difference
from task_6_number_sundays import total_sunday_counts
from task_7_week_number_birthdate import week_number
from task_8_calendar_birth_month import month_calendar
from task_9_days_till_next_birthday import number_days
from task_10_leap_years import get_leap_years


date = input("Write your date of birth in the numerical format Year-Month-Day: ")
print(f"You were born on a {gw1(date)}.")
print(f"You were born on the day number {dn1(date)} of the year")
print(f"You were born on the week number {week_number(date, '%Y-%m-%d')} of the year")
print(month_calendar(date))


print(f"You have lived {total_sunday_counts(date)} Sunday so far")
print(f"You have lived {len(get_leap_years(date))} leap year so far. The leap years are:\n{get_leap_years(date)}")


print(f"This year, your birthday is on a {gw2(date)}")
print(f"There are {number_days(date, '%Y-%m-%d')} until your next birthday")
