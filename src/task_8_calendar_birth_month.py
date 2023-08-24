import calendar
import datetime  # Don't forget to import the datetime module

def month_calendar(date_string):
    """
    Returns the calendar of the month of birth ready to print.

    :param date_string: Birthdate in the format "Year-Month-Day"
    :return: The calendar of the birth month
    """
    # Convert the input string to a datetime object
    birthdate = datetime.datetime.strptime(date_string, "%Y-%m-%d")
    
    # Get the month and year of the birthdate
    birth_month = birthdate.month
    birth_year = birthdate.year
    
    # Generate the calendar for the birth month and year
    cal = calendar.month(birth_year, birth_month)
    
    return cal

calendar_output = month_calendar("2000-03-15")
print("Calendar of the birth month:")
print(calendar_output)
