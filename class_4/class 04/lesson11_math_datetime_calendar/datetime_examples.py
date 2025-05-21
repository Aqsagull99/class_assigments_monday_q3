from datetime import datetime, timedelta

# Current date and time
now = datetime.now()
print("Current datetime:", now)

# Formatting dates
print("Formatted date:", now.strftime("%Y-%m-%d %H:%M:%S"))

# Date arithmetic
future_date = now + timedelta(days=7)
print("Date one week from now:", future_date)