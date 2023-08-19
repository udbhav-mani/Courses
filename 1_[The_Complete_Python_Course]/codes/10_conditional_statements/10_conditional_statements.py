num = "20"
user_input = input("Enter number ")
if user_input == num:
    print("Same numbers!!")
else:
    print("Not Same numbers!!")


tuple1 = ("a", "b", "c")
tuple2 = ("d", "e")

check = input("Enter a character: ")
if check in tuple1:
    print("In tuple 1")
elif check in tuple2:
    print("In tuple 2")
else:
    print("nowhere")
