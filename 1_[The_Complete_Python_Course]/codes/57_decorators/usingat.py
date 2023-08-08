import functools

user = [
    {"name": "raj", "role": "admin"},
    {"name": "rohan", "role": "guest"},
]


def check_access(fun):
    @functools.wraps(fun) #tells has_access that it wraps fun
    def has_access():
        if user[1]["role"] == "admin":
            return fun()
        else:
            raise PermissionError("Not allowed")

    return has_access


@check_access #this represents hidden = check_access(hidden)
def hidden():
    print("Very Very secret text!!")


hidden()
