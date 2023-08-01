from collections import namedtuple

# to give each element of tuple a name

Friend = namedtuple("Friend", ["name", "salary"])

friend = Friend("abhi", 45678,)

print(friend)
