from datetime import datetime
from dateutil.relativedelta import relativedelta

# Input: Date of birth from user
dob_str = input("Enter your date of birth (YYYY-MM-DD): ")
dob = datetime.strptime(dob_str, "%Y-%m-%d")

# Today's date
today = datetime.today()

# Calculate the difference
difference = relativedelta(today, dob)

# Print age in years, months, and days
print(f"You are {difference.years} years, {difference.months} months, and {difference.days} days old.")
