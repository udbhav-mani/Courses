from collections import OrderedDict
from pprint import pprint

# Question: Complete the script so that it removes duplicate items from the list a .

a = ["1", 1, "1", 2]
# Expected output:

#   ['1', 2, 1]
a = set(list(a))
pprint(a)

# a = list(OrderedDict.fromkeys(a))
# print(a)
