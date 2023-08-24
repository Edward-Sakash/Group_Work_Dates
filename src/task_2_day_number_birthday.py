import datetime
from task_0 import extract_birthday

def day_num_in_year(date_string):
    """
    Returns the day number of the birthday in the current year.

    :param date_string: A string in the format "Year-Month-Day"
    :return: The day number of the birthday
    """
    # Get the birthday datetime object with the current year
    birthday = extract_birthday(date_string)
    
    # Get the day number of the year using the `timetuple()` method
    day_number = birthday.timetuple().tm_yday
    
    return day_number

"""day_number = day_num_in_year("2000-03-15")
print(day_number)"""

