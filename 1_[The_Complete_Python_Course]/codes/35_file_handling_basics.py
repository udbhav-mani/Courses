

file = open("any_example_file.txt", "w")
file_contents = file.read()
# we can also open and close a file with the help of a context manager

with open("any_example_file.txt", "w") as file:
    contents = file.read()