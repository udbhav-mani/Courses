list1 = [1, 2, 3, 4, 5, 6, 7, 8]

# if we want to have a list with list elements doubled, we can
new_list = []
for numbers in list1:
    new_list.append(numbers * 2)

print(new_list)

# another approach
new_list = [numbers * 2 for numbers in list1]  # [2, 4, 6, 8, 10, 12, 14, 16]
print(new_list)

# we can also add conditions like
new_list = [numbers * 2 for numbers in list1 if numbers % 2 == 0]  # [4, 8, 12, 16]
print(new_list)
