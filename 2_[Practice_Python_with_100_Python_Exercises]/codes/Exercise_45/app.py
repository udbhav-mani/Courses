import string, os

letters = string.ascii_lowercase

if not os.path.exists("letters"):
    os.makedirs("letters")

for letter in letters:
    with open(f"letters/{letter}.txt", "w") as file:
        file.write(letter)
    