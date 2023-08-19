from string import ascii_uppercase as letters


def generate_alphabets():
    with open("abc.txt", "w") as file:
        for letter in letters:
            file.write(f"{letter}\n")


generate_alphabets()
