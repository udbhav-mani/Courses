friends = [["asd", 1], ["qwe", 2], ["tyu", 3], ["okj", 4], ["mnb", 5]]


def details(name, id):
    print(name, id)


for friend in friends:
    details(name=friend[0], id=friend[1])

# else we can do this
for friend in friends:
    details(*friend)  # passes arguments as no of parameters
