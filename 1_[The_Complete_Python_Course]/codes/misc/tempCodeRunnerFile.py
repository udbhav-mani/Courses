a = 256999
b = a
c = b
b += 1
print(id(a))
print(id(b))
print(id(c))
print(b.__class__)
