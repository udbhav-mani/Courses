import requests

contents = requests.get(
    "https://pythonhow.com/media/data/universe.txt",
    headers={"user-agent": "customUserAgent"},
).text
print(contents)
