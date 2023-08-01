friends = [
    {"name": "asd", "age": 1},
    {"name": "qwe", "age": 2},
    {"name": "tyu", "age": 3},
    {"name": "mnb", "age": 4},
]


def details(name, age):
    print(name, age)


for friend in friends:
    details(name=friend["name"], age=friend["age"])

# else we can do this
for friend in friends:
    details(**friend)  # passes arguments as named parameters order wise
