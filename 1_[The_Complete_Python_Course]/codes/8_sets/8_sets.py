# no order preserved and no duplicates
# {}, add, remove

set1 = {"a", "c"}
print(set1)

# set operations
set2 = {"c", "d", "e"}
print(set1.difference(set2))
print(set2.difference(set1))

print(set1.symmetric_difference(set2))  # not in both
print(set2.intersection(set1))
print(set2.union(set1))
