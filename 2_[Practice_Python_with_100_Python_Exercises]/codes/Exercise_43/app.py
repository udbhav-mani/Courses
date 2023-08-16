"""
Question: Create a script that generates a file where all letters of the English alphabet are listed two in each line. The inside of the text file would look like:

ab
cd
ef

and so on.
"""
import string

letters = string.ascii_lowercase
# with open("ab.txt", "w") as file:
#     for i in range(0, len(letters), 2):
#         file.write(f"{letters[i]}{letters[i+1]}\n")

with_a = letters[::2]
with_b = letters[1::2]

with open("ab.txt", "w") as file:
    for x, y in zip(with_a, with_b):
        file.write(x + y + "\n")
