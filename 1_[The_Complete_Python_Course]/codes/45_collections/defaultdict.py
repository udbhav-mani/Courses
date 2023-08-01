#  if we try to access a key that does not exist, it gives a keyerror
# so we add a default value to a dict so that it doest give so

from collections import defaultdict


friend = {
    "ghj": ["uhj", "hjk", "ghjk"],
    "vgu": ["tg", "hfjk", "gfd"],
    "uh": ["yt", "trfd", "ee"],
}

friend = defaultdict(list, friend)
friend["ghj"] = ["uhj", "hjk", "ghjk"]
# or we can make a new dict by friend = defaultdict(list) and then add to the dict

# print(friends["ghj"])
# friends["yugh"] = "yhj"

print(friend["wsedrf"])
print(friend["ghj"])

# we can also pass a funtion inside the defaultdict function