file = open("file.txt", "+a")
while True:
    user_input = input("Enter something - ")
    if user_input == "CLOSE":
        break
    elif user_input == "SAVE":
        file.close()
        file = open("file.txt", "+a")
    else:
        file.write(user_input + "\n")
