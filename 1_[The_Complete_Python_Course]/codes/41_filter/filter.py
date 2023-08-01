def filter_names(names):
    return names.startswith("a")


names = ["abc", "def", "ghi", "akl", "mno"]

# names_starting_with_a = filter(filter_names, names)
# names_starting_with_a2 = filter(lambda x: x.startswith("r"), names)

# alsosame
names_starting_with_a = (name for name in names if name.startswith("a"))

print(list(names_starting_with_a))
# print(list(names_starting_with_a2))
