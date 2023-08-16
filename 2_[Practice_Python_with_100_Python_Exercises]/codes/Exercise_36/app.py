def count_words():
    with open("words1.txt", "r") as file:
        contents = file.read()
    return len(contents.strip().split())


print(count_words())
