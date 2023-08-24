import datetime
import calendar

def get_leap_years(date_string):
    """
    Returns a list of the leap years since the birthdate.
    :param date_string: The birthdate in the format "%Y-%m-%d"
    :return: A list of the leap years
    """
    # Convert the input string to a datetime object
    birthdate = datetime.datetime.strptime(date_string, "%Y-%m-%d")
    
    # Get the birth year
    birth_year = birthdate.year
    
    # Get the current year
    current_year = datetime.datetime.now().year
    
    # Create a list to store leap years
    leap_years = []
    
    # Iterate through years from the birth year to the current year
    for year in range(birth_year, current_year + 1):
        if calendar.isleap(year):
            leap_years.append(year)
    
    return leap_years

leap_years = get_leap_years("2000-03-15")
print("Leap years since the birthdate:", leap_years)
