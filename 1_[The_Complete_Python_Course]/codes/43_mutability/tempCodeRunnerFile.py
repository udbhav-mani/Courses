def change_age(age):
    print(id(age))
    age = age + 1
    print(id(age))


a = 19
print(id(a))
change_age(a)