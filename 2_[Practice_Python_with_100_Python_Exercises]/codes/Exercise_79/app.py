def validate_password(password):
    result1 = any(char.isdigit() for char in password)
    result2 = any(char.isupper() for char in password)
    result3 = len(password) >= 5
    return result1 and result2 and result3


while True:
    password = input("Enter password - ")
    if validate_password(password=password):
        print("Password is fine.")
        break
    else:
        print("Password is not fine.")
