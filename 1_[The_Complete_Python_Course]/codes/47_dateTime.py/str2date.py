from datetime import datetime, timedelta, timezone

print(datetime.now(timezone.utc) + timedelta(days=12, hours=2))

# string format time
current_time = datetime.now(timezone.utc)
print(current_time.strftime("%d:%m:%Y, %H-%M-%S"))
user_input = input("Enter date time in DD-MM-YYYY format")
print(datetime.strptime(user_input, "%d:%m:%Y"))
