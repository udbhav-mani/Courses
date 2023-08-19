import string

with open("countries_raw.txt", "r") as file:
    contents = file.read().strip().split("\n")
contents = [content for content in contents if content != ""]
contents = [content for content in contents if content != "Top of Page"]
contents = [content for content in contents if content not in string.ascii_uppercase]

with open("countries_clean.txt", "w") as file:
    for country in contents:
        print(contents)
        # file.seek(0)
        file.write(country + "\n")
        # file.truncate()
