a = [1, 2, 3]
b = (4, 5, 6, 7, 5)

for x, y in zip(a, b):
    print(x + y)

print(list(zip(a, b)))
