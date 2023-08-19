def validate_password(password):
    result1 = any(char.isdigit() for char in password)
    result2 = any(char.isupper() for char in password)
    result3 = len(password) >= 5

    errors = list()
    if not result3:
        errors.append("Length is less than 5!")
    if not result2:
        errors.append("An uppercase letter is missing in the password!")
    if not result1:
        errors.append("A number is missing in the password!")

    return errors


while True:
    password = input("Enter password - ")
    errors = validate_password(password=password)
    if len(errors) == 0:
        print("Password is fine.")
        break
    else:
        for error in errors:
            print(error)
