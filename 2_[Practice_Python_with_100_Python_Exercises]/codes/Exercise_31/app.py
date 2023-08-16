def foo(a=1, b=2):
    return a + b


# x = foo - 1 error as foo should be called
x = foo() - 1
