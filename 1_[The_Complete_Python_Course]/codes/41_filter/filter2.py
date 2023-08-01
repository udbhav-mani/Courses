# same as filter
def custom_filter(func, iterable):
    for i in iterable:
        if func(i):
            yield i


names = ["abc", "def", "ghi", "akl", "mno"]

names_starting_with_a = custom_filter(lambda x: x.startswith("a"), names)

print(next(names_starting_with_a))
print(next(names_starting_with_a))
