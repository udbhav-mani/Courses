#  ordered in the way they are added
from collections import OrderedDict

friends = OrderedDict()
friends["wer"] = 0
friends["fd"] = 1
friends["re"] = 2
friends["gv"] = 3

print(friends)
friends.move_to_end("wer")
print(friends)
friends.move_to_end("wer", last=False)
print(friends)
