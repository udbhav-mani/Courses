while True:
    user_input = input("Enter a number ")
    try:
        user_input = int(user_input)
    except ValueError:
        print("Please enter a valid number!! ")
    else:
        if user_input % 2 == 0:
            print("Even Number")
        else:
            print("Odd Number!!")
    finally:
        user_choice = input("Want to play again ?? (y/n) ")

    if user_choice != "y":
        break
