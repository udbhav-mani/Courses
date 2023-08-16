l1 = ["a", "aax", "cfd"]
l2 = [x for x in l1 if x.startswith("c")]


print("List 1 - ")
print(id(l1))
print(id(l1[0]))
print(id(l1[1]))
print(id(l1[2]))
l1[2] = "jhg"
print(id(l1[2]))
print(l1)

print("List 2 - ")
print(id(l2))
print(id(l2[0]))
# print(id(l2[1]))
# print(id(l2[2]))
print(l2)


# print(id(l1[0]) == id(l2[0]))
