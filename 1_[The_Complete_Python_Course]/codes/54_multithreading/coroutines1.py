def greet():
    while True:
        print("Before Yield")
        greeting = yield
        print(f"{greeting}, World")
        print("After Yield")


g = greet()
next(g)
# g.send(None)
g.send("hello")
# g.send("hi")
# g.send(None)
# g.send("hello")
