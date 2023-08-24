import datetime

def week_number(date_string, date_format):
    """
    Returns the week number of the birthdate in the birth year.

    :param date_string: The birthdate in the format "Year-Month-Day"
    :param date_format: The format of the date, e.g., "%d/%m/%Y"
    :return: The week number of the birthdate
    """
    # Convert the input string to a datetime object using the provided date format
    birthdate = datetime.datetime.strptime(date_string, date_format)
    
    # Get the ISO calendar week number of the birthdate
    week_number = birthdate.isocalendar()[1]
    
    return week_number

week_num = week_number("2000-03-15", "%Y-%m-%d")
print("Week number:", week_num)
