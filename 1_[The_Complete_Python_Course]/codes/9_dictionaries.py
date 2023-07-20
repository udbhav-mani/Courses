# changeable, addable, ordered kept, no duplicate keys
# key - value pairs like {"key": "value"}
# dict = {1: "a", 2: "b", 3: "c"}

dict1 = {"rahul": 1, "raj": 2, "rohan": 3, "ram": 4}
print(dict1)

dict1["rohit"] = 5
print(dict1)
dict1["raj"] = 6
print(dict1)

make_dict = dict(a=11, b=22, d=33)
print(make_dict)

to_dict = (["a", 1], ["b", 2], ["c", 3], ["d", 4])
dict2 = dict(to_dict)
print(dict2)
# can also be made from list of tuples

tuple_dict = (
    {"key1": "value1", "key1_1": "value1_1"},
    {"key2": "value2"},
    {"key3": "value3"},
    {"key4": "value4"},
)

print(tuple_dict[0])
print(tuple_dict[0]["key1_1"])
