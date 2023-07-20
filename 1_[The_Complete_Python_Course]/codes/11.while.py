user_input = input("Do you wish to play a game?? ")
while user_input == "yes":
    number = int(input("Enter a number - "))
    if number % 2 == 0:
        print("Even Number!! ")
    else:
        print("Odd Number!! ")
    user_input = input("Do you still wish to play the game?? ")


print("Thank you for playing.")
