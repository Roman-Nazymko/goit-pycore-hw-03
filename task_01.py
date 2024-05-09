from datetime import datetime

def get_days_from_today(date):
   try:
       # Convert the input date string into a datetime object
       date_object = datetime.strptime(date, "%Y-%m-%d")

        # Get the current date
       current_date = datetime.today()

       # Calculate the difference between the current date and the input date
       difference_in_days = current_date - date_object

       # Return the difference in days
       return difference_in_days.days
   
   except ValueError:
       # Handle the case where the input date format is incorrect
       return "Invalid date format. Enter date in 'YYYY-MM-DD' format."

# Test the function
print(get_days_from_today("1993-04-01"))   