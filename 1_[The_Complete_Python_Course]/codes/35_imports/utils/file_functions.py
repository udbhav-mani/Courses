def save_to_file(filename, contents):
    with open(filename, "w") as file:
        file.write(contents)


def read_from_file(filename):
    with open(filename, "r") as file:
        contents = file.read()

    print(contents)
