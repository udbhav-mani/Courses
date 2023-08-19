from datetime import datetime

user_input = int(input("Enter your age - "))
current_year = datetime.now().year
print("We think you were born back in %s" % (current_year - user_input))
