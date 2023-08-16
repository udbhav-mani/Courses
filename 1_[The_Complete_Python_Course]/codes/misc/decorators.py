import time

nums = [1, 2, 3, 4, 5, 6]


def timing(fun):
    def timer(*args):
        start = time.time()
        result = fun(*args)
        print(f"{time.time() - start:.9f}")
        return result

    return timer


def display_result(fun):
    def display(*args):
        print(fun(*args))

    return display


# @timing
@display_result
def calculate(a):
    total = 0
    for num in nums:
        total += num**a

    return total


# calculate = timing(calculate)


calculate(3)
