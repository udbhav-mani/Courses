class Friend:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # as it is a method that uses nothing other than self, we can
    # also consider and make it a property
    @property
    def print(self):
        print(f"Hello, {self.name}.")


rahul = Friend("rahul", 20)
rohit = Friend("rohit", 22)

# can use as a property here
rohit.print
