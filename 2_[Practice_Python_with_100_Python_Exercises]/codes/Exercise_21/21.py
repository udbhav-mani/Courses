# Question: Filter the dictionary by removing all items with a value of greater than 1.

d = {"a": 1, "b": 2, "c": 3}
# Expected output:

{"a": 1}

dict1 = {key: d[key] for key in d if d[key] == 1}
dict2 = dict([(key, value) for key, value in d.items() if value <= 1])
print(dict1)
print(dict2)
