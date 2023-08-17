import requests

contents = requests.get(
    "https://pythonhow.com/media/data/universe.txt",
    headers={"user-agent": "customUserAgent"},
)
text = contents.text

print(text.count("a"))


# count = 0
# for letter in text:
#     if letter == "a":
#         count += 1

# print(count)
