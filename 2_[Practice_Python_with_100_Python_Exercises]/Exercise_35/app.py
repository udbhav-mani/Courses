# Create a function that takes any string as input and
# returns the number of words for that string.

str = "Hello this is me"


def count_words(str):
    str = str.split()  # default for split is white spaces
    return len(str)


print(count_words(str))
