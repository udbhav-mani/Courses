"""
To add a number to a string, we can use str(num)
Below are all the other ways -
"""

num = 30
str1 = "Thirty - {}"
str2 = "Thirty - {number}"

print("Thirty - "  + str(num))
print(f"Thirty - {num}")
print("Thirty - {}".format(num))
print("Thirty - {number}".format(number = num))
print(str1.format(num))
print(str2.format(number = num))
