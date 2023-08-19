d = {
    "employees": [
        {"firstName": "John", "lastName": "Doe"},
        {"firstName": "Anna", "lastName": "Smith"},
        {"firstName": "Peter", "lastName": "Jones"},
    ],
    "owners": [
        {"firstName": "Jack", "lastName": "Petter"},
        {"firstName": "Jessy", "lastName": "Petter"},
    ],
}
d["employees"].append({"firstName": "Rolf", "lastName": "Jackson"})

print(d["employees"])
