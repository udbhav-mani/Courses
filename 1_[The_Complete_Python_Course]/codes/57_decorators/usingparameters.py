import functools

user = [
    {"name": "raj", "role": "admin"},
    {"name": "rohan", "role": "guest"},
]


def check_access(fun):
    @functools.wraps(fun)  # tells has_access that it wraps fun
    def has_access(param):
        if user[0]["role"] == "admin":
            return fun(param)
        else:
            raise PermissionError("Not allowed")

    return has_access


@check_access  # this represents hidden = check_access(hidden)
def hidden(
    param,
):  # to pass parameters here, ensure that has_access() accepts parameter too
    print(f"Very Very secret text - {param} !!")


hidden("password123")
