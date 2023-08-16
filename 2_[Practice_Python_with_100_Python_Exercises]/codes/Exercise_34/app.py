def foo():
    global c  # we can change the global variables inside any fun scope just by using global keyword
    c = 1
    return c


foo()
print(c)
