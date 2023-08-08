user = [
    {"name": "raj", "role": "admin"},
    {"name": "rohan", "role": "guest"},
]


def check_access(fun):
    print("Inside check_access 1!")

    def has_access():
        print("Inside 1st!")
        if user[0]["role"] == "admin":
            print("Inside 2nd!")
            return fun()
        else:
            raise PermissionError("Not allowed")

    print("before return 1st point!")
    return has_access


def hidden():
    print("Inside point hidden!")
    print("Very Very secret text!!")


ret_value = check_access(hidden)
ret_value()
