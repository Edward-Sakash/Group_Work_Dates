import datetime

def get_birthday_difference(first_birthday, second_birthday):
    """
    Returns the difference in days between two birthdates.

    :param first_birthday: A string in the format "Year-Month-Day" for the first birthdate
    :param second_birthday: A string in the format "Year-Month-Day" for the second birthdate
    :return: The difference in days between the two birthdates
    """
    # Convert the strings to datetime objects
    first_date = datetime.datetime.strptime(first_birthday, "%Y-%m-%d")
    second_date = datetime.datetime.strptime(second_birthday, "%Y-%m-%d")
    
    # Calculate the difference in days
    difference = (first_date - second_date).days
    
    return abs(difference)

difference = get_birthday_difference("2000-03-15", "1995-12-25")
print("Difference in days:", difference)

