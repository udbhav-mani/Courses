user_input = input("Enter string - ")
user_input = user_input.strip().split(",")

with open("data.csv", "+a") as file:
    for line in user_input:
        file.write(line + "\n")
