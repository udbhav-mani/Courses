def write_to_file(nearby_friends):
    file = open(
        "1_[The_Complete_Python_Course]/codes/31_file_handling/31_nearby_friends.txt",
        "w",
    )
    for friend in nearby_friends:
        print(f"{friend} is nearby !! ")
        file.write(friend + "\n")
    file.close()


user_input = input("Enter the names of three friends (separated be comma) ")
user_input = set(user_input.split(","))

friends_file = open(
    "1_[The_Complete_Python_Course]/codes/31_file_handling/31people.txt",
    "r",
)
friends = friends_file.read()
friends_file.close()
friends = set(friends.split("\n"))

nearby_friends = user_input.intersection(friends)

write_to_file(nearby_friends)
