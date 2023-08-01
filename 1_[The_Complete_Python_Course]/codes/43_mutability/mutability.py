# list float string tuples are immutable
# when we add to lists, the ist id remains same

list1 = [1, 2]
print(id(list1))
list1.append(3)
print(id(list1))
# the above two will have the same id
my_int = 5
print(id(my_int))
my_int = 6
print(id(my_int))
#  but these two will not be same as int is immutable
#  all functions return new int or immutable objects
#  but in immutable, object is changed


