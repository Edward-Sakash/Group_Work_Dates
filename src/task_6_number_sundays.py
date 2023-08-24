import datetime

def total_sunday_counts(date_string):
    """
    Counts the occurrence of Sundays since the birthdate until the current date.

    :param date_string: The birthdate in the format "Year-Month-Day"
    :return: The total occurrence of Sundays
    """
    # Convert the input string to a datetime object
    birthdate = datetime.datetime.strptime(date_string, "%Y-%m-%d")
    
    # Get the current date
    current_date = datetime.datetime.now()
    
    # Calculate the difference in days between birthdate and current date
    days_difference = (current_date - birthdate).days
    
    # Initialize a counter for Sundays
    sunday_count = 0
    
    # Iterate through each day in the range and count the Sundays
    for i in range(days_difference + 1):
        current_day = birthdate + datetime.timedelta(days=i)
        if current_day.weekday() == 6:  # Sunday has index 6
            sunday_count += 1
    
    return sunday_count

sunday_count = total_sunday_counts("2000-03-15")
print("Total Sundays:", sunday_count)
