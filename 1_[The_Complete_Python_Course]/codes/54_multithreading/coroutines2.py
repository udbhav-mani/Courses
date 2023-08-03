from collections import deque

friends = deque(("Rolf", "Jose", "Charlie", "Jen", "Anna"))


def friend_upper():
    while friends:
        friend = friends.popleft().upper()
        print("In second function, before yield")
        greeting = yield
        print("In second function, after yield")
        print(f"{greeting}, {friend}")


def greet(g):
    print("In first function, before priming")
    g.send(None)
    print("In first function, after priming")
    while True:
        print("In first function, before yield")
        greeting = yield
        print("In first function, after yield")
        g.send(greeting)


greeter = greet(friend_upper())

greeter.send(None)
print("Sending hello")
greeter.send("Hello")
# print("Hello, world! Multitasking...")
# greeter.send("How are you,")
