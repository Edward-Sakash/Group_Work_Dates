import datetime
import calendar

def get_weekday(date_string):
    """
    Gets the weekday corresponding to the provided date_string in the format "Year-Month-Day".

    :param date_string: A string in the format "Year-Month-Day"
    :return: The weekday corresponding to the provided date_string
    """
    # Parse the provided date string into a datetime.datetime object
    birthdate = datetime.datetime.strptime(date_string, "%Y-%m-%d")
    
    # Get the day of the week (0 = Monday, 6 = Sunday)
    weekday_number = birthdate.weekday()
    
    # Get the weekday name using the calendar module
    weekday_name = calendar.day_name[weekday_number]
    
    return weekday_name

"""weekday = get_weekday("2000-03-15")
print(weekday)
"""