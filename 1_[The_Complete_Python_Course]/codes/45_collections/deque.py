from collections import deque

friends = deque(("hrllo", "fsd", "tfg"))
print(friends)
friends.append("bhjm")
print(friends)
friends.appendleft("kjhb")
print(friends)
friends.pop()
print(friends)
