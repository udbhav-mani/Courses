import string, os, glob

files = glob.glob("letters/*txt")  # we can traverse this to get files

letters = string.ascii_lowercase
l = list()

for letter in letters:
    with open(f"letters/{letter}.txt", "r") as file:
        contents = file.read()
        l.append(contents)

print(l)
