
from collections import deque
from types import coroutine

friends = deque(("Rolf", "Jose", "Charlie", "Jen", "Anna"))

@coroutine
def friend_upper():
    while friends:
        friend = friends.popleft().upper()
        print("In second function, before yield")
        greeting = yield
        print("In second function, after yield")
        print(f"{greeting}, {friend}")


async def greet(g):
    await g


greeter = greet(friend_upper())

greeter.send(None)
print("Sending hello")
greeter.send("Hello")
# print("Hello, world! Multitasking...")
# greeter.send("How are you,")
