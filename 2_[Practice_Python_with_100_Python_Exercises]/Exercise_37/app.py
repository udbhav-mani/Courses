# def count_words():
#     with open("words2.txt", "r") as file:
#         contents = file.read()
#         contents = contents.replace(",", " ")
#     return len(contents.split())


# print(count_words())


import re


def count_words_re(filepath):
    with open(filepath, "r") as file:
        text = file.read()
    string_list = re.split(",| ", text)  # comma or spaces
    return len(string_list)


print(count_words_re("words2.txt"))
