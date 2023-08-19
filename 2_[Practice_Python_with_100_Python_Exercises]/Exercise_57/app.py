import json
from pprint import pprint

with open("company1.json", "r") as file:
    contents = json.load(file)

pprint(contents)
