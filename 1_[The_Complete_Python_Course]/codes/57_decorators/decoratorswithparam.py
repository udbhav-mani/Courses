import functools

user = [
    {"name": "raj", "role": "admin"},
    {"name": "rohan", "role": "guest"},
]


def third_level(access):
    def check_access(fun):
        @functools.wraps(fun)  # tells has_access that it wraps fun
        def has_access(param):
            if user[1]["role"] == access:
                return fun(param)
            else:
                raise PermissionError("Not allowed")

        return has_access

    return check_access


@third_level("guest")
def hidden(
    param,
):  # to pass parameters here, ensure that has_access() accepts parameter too
    print(f"Very Very secret text - {param} !!")


hidden("password123")
