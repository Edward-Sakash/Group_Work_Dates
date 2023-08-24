import datetime

def number_days(date_string, date_format):
    """
    Returns the number of days until the next birthday.

    :param date_string: The birthdate
    :param date_format: The format (recognized by datetime module)
    :return: The number of days until the next birthday
    """
    # Convert the input string to a datetime object using the provided date format
    birthdate = datetime.datetime.strptime(date_string, date_format)
    
    # Get the current date
    current_date = datetime.datetime.now()
    
    # Calculate the next birthday in the current year
    next_birthday = birthdate.replace(year=current_date.year)
    if next_birthday < current_date:
        next_birthday = next_birthday.replace(year=current_date.year + 1)
    
    # Calculate the difference in days
    days_until_next_birthday = (next_birthday - current_date).days
    
    return days_until_next_birthday

days_until_next_birthday = number_days("2000-03-15", "%Y-%m-%d")
print("Number of days until the next birthday:", days_until_next_birthday)
