import datetime

def extract_birthday(date_str):
    """
    Extracts the birthdate from the provided date_string and returns a datetime.datetime object with the current year.

    :param date_str: A string in the format "Year-Month-Day"
    :return: A datetime.datetime object representing the birthdate with the current year
    """
    today = datetime.datetime.today()  # Get the current date and time
    year = today.year  # Get the current year
    
    # Parse the provided date string into a datetime.datetime object
    birthdate = datetime.datetime.strptime(date_str, "%Y-%m-%d")
    
    # Create a new datetime object with the current year and the birthdate's month and day
    birthday = datetime.datetime(year, birthdate.month, birthdate.day)
    
    return birthday

