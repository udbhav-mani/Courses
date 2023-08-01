names = ["abc", "def", "ghi", "akl", "mno"]


# maps it to value returned by anither function
names_starting_with_a = map(lambda x: x.title(), names)
# names_starting_with_a2 = filter(lambda x: x.startswith("r"), names)

# alsosame
# names_starting_with_a = (name for name in names if name.startswith("a"))
# names_starting_with_a = (name.title() for name in names)

print(list(names_starting_with_a))
# print(list(names_starting_with_a2))
