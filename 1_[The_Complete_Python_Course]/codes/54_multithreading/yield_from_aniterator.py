from collections import deque

friends = deque(("a", "b", "c", "d", "e", "f", "g", "h"))


def get_friends():
    yield from friends


def call_get(func):
    while True:
        try:
            friend = next(func)
            yield friend
        except StopIteration:
            pass


generator = get_friends()
print(next(call_get(generator)))
print(next(call_get(generator)))
print(next(call_get(generator)))
print(next(call_get(generator)))
print(next(call_get(generator)))
print(next(call_get(generator)))
print(next(call_get(generator)))
print(next(call_get(generator)))
print(next(call_get(generator)))
