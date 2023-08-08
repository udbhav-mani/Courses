def check_access(fun):
    @functools.wraps(fun)  # tells has_access that it wraps fun
    def has_access(param):
        if user[0]["role"] == "admin":
            return fun(param)
        else:
            raise PermissionError("Not allowed")

    return has_access


@check_access 