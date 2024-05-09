from datetime import datetime, timedelta

def get_upcoming_birthdays(users: list) -> list:
    today = datetime.today().date()
    birthday_list = []

    for user in users:
        # Convert the birthday string to a datetime.date object
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        # Set the year to the current year since it might have already passed this year
        birthday_this_year = birthday.replace(year=today.year)

        # If the birthday has already passed this year, move it to next year
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        
        # Calculate the number of days until the next birthday
        days_to_birthday = (birthday_this_year - today).days

        # If the birthday is less than 7 days away
        if 0 <= days_to_birthday < 7:
            # Determine the congratulation date
            congratulation_date = today + timedelta(days=days_to_birthday)

            # If the birthday falls on a weekend, congratulate on the next working day
            if birthday_this_year.weekday() >= 5:
                next_monday = today + timedelta(days=(7 - today.weekday()))
                congratulation_date = next_monday

            # Add the name and congratulation date to the list
            birthday_list.append({"name": user["name"], "congratulation_date": congratulation_date.strftime("%Y.%m.%d")})
    
    return birthday_list        

# Create a list of users
users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "John Smith", "birthday": "1991.05.12"},
    {"name": "Rick Novak", "birthday": "1995.05.15"}
]

# Get the list of upcoming birthdays
upcoming_birthdays = get_upcoming_birthdays(users)
print("List of congratulations for this week:", upcoming_birthdays)
