nums = (1, 2, 3, 4)


def add_all(a, b, c, d):
    return a + b + c + d


def add_all2(*num):
    return sum(num)


def add_all3(a, b, c, d):
    return a + b + c + d


def add_all4(**kwargs):
    print(kwargs)


print(add_all(*nums))
print(add_all2(3, 4, 5, 6))

numdict = {"a": 5, "b": 4, "c": 3, "d": 2}

print(add_all3(**numdict))
print(add_all4(username="user", id=1))
