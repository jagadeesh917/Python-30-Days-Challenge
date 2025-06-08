from datetime import datetime
from dateutil.relativedelta import relativedelta

date1 = datetime(2025, 6, 7)
date2 = datetime(2025, 5, 27)

date3 = datetime(2020, 3, 7)
date4 = datetime(2025, 5, 27)

difference1 = date1 - date2
difference2 = relativedelta(date4,date3)

print(f"Days between the two dates are : {difference1.days}")
print(f"Years/Months/Days between the two dates are : {difference2.years} years {difference2.months} months {difference2.days} days")
