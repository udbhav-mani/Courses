"""
Question: Create a script that generates a file where all letters of the English alphabet are listed two in each line. The inside of the text file would look like:

ab
cd
ef

and so on.
"""
import string

letters = string.ascii_lowercase + " " # for yz to come and not get ignored in slice

with open("abc.txt", "w") as file:
    for x, y, z in zip(letters[::3], letters[1::3], letters[2::3]):
        file.write(x + y + z + "\n")
