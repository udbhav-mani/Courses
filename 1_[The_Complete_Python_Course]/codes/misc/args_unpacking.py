def mult(*args):  # can even take empty args
    return args


def add(x, y):
    return x + y


def named(**kwargs):
    return kwargs


def both(*args, **kwargs):
    print(args)
    print(kwargs)


# print(mult(9, 10, 11))
# print(mult())
# print(add(**{"x": 1, "y": 2}))

# dic = {"name": "Bob", "age": 12}
# print(named(name="Bob", age=12))
# print(named(**dic))
#
both(1, 5, 7, name="Bob", age=12)
