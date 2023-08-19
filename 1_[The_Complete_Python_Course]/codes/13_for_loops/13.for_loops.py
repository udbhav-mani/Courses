# break and continue work the same
tuple = (
    "a",
    "b",
    "c",
    "d",
    "e",
)


for element in tuple:
    print(element)
else:
    print("Run succesful")  # runs when the forloop runs successfully

elements = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for element in elements:
    print(f"Loop ran for {element+1} times.")

# using range() from 0 to n-1
for element in range(9):
    print(f"Loop ran for {element+1} times.")

for element in range(0, 9):
    print(f"Loop ran for {element+1} times.")

# using range() from 0 to n-1 by 2
for element in range(0, 9, 2):
    print(f"Loop ran for {element+1} times.")

dict1 = {"rahul": 1, "raj": 2, "rohan": 3, "ram": 4}

# we iterate over dict keys
# prints only keys
for element in dict1:
    print(element)

# prints value of the keys (2 methods)
for element in dict1:
    print(dict1[element])
##second method - using values()
for element in dict1.values():
    print(element)

# for getting key-value pairs use items()
for name, id in dict1.items():
    print(name, id)
