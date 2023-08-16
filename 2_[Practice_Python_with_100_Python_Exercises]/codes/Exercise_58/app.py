import json
from pprint import pprint


with open("company1.json", "r+") as file:
    contents = json.load(file)
    contents["employees"].append({"firstName": "Albert", "lastName": "Bert"})
    file.seek(0)
    json.dump(contents, file, indent=4)
    file.truncate()


# print(contents)
