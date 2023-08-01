import re


def is_filename_safe(filename):
    # you only need to change the regular expression (regex) below
    regex = "[a-zA-Z0-9][a-zA-Z0-9\-\_\(\)]*(\.jpg|\.jpeg|\.png|\.gif)$"
    print(re.match(regex, filename)[0])
    print(re.match(regex, filename)[0] == filename)


is_filename_safe("1.jpg")
is_filename_safe("test.jpg")
is_filename_safe("tyuik.jpg")
is_filename_safe("pokj.gif.jpg")
