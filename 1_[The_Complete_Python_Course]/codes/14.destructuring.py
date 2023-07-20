dogs_with_age = [["lab", 10], ["golden", 12], ["husky", 13]]

# destructuring here to get both together rather than using a single element to save lists
for name, age in dogs_with_age:
    print(name, age)

example_tuple = (
    ("a"),
    ("b"),
    ("c"),
)
#destructuring
element1, element2, element3 = example_tuple

print(element1)
print(element2)
print(element3)
