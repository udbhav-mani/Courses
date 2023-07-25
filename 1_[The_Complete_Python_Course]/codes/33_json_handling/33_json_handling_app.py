import json

#allows lists and dictionaries but not strings

file = open("sample.json", "w")
json.dump(
    {
        "friends": [
            {"name": "Rolf", "age": 22},
            {"name": "Helen", "age": 21},
            {"name": "Anna", "age": 23},
        ]
    },
    file,
)
file.close()

# we can also use json.loads and dumps

file = open("sample.json", "r")
contents = json.load(file)
print(contents)
file.close()
