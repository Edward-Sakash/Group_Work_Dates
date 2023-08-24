import datetime
from task_0 import extract_birthday

def day_num_in_year(date_string):
    """
    Returns the day number of the birthdate in the birth year.

    :param date_string: A string in the format "Year-Month-Day"
    :return: The day number of the birthdate in the birth year
    """
    # Get the birthday datetime object
    birthday = extract_birthday(date_string)
    
    # Get the day of the year (1 = January 1)
    day_of_year = birthday.timetuple().tm_yday
    
    return day_of_year

# Test the function with an example date
day_number = day_num_in_year("2000-03-15")
print("Day number in birth year:", day_number)
