import functools

user = [
    {"name": "raj", "role": "admin"},
    {"name": "rohan", "role": "guest"},
]


def check_access(fun):
    @functools.wraps(fun)  # tells has_access that it wraps fun
    def has_access(*args, **kwargs):
        if user[0]["role"] == "admin":
            return fun(*args, **kwargs)  # any number of args or named args
        else:
            raise PermissionError("Not allowed")

    return has_access


@check_access  # this represents hidden = check_access(hidden)
def hidden():  # making it generic
    print(f"Very Very secret text !!")


hidden("password123")
