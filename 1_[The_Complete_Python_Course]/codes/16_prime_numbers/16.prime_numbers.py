user_input = int(input("Enter a number - "))
for number in range(2, user_input):
    for n in range(2, number):
        if number % n == 0:
            print(f"{number} is not prime as 33{n} * {number//n} = {number}")
            break
    else:
        print(f"{number} is  PRIME!")
