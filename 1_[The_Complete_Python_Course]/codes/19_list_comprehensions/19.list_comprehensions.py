# List comprehensions
name_list = ["abc", "def", "ghi", "jkl", "mno"]
friend_list = ["vwx", "stu", "pqr", "jkl", "mno"]
name_list_title = [name.title() for name in name_list]
print(name_list_title)

# multiple statements in one can be reduced if it makes the code cluttered

answer_list = [name.upper() for name in friend_list if name in name_list]
print(answer_list)

# we have similar for set and dictionary comprehensions with {}