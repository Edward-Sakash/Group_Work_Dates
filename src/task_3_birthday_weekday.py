import datetime
import calendar
from task_0 import extract_birthday

def get_weekday(date_string):
    """
    Gets the weekday corresponding to the birthday in the current year of the provided date_string.

    :param date_string: A string in the format "Year-Month-Day"
    :return: The weekday corresponding to the birthday
    """
    # Get the birthday datetime object with the current year
    birthday = extract_birthday(date_string)
    
    # Get the day of the week (0 = Monday, 6 = Sunday)
    weekday_number = birthday.weekday()
    
    # Get the weekday name using the calendar module
    weekday_name = calendar.day_name[weekday_number]
    
    return weekday_name

# Test the function with an example date
birthday_weekday = get_weekday("2000-03-15")
print("Birthday weekday:", birthday_weekday)

