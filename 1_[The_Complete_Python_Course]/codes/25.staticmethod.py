class Friend:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def print(self):
        print(f"Hello, {self.name}.")

    # as it doesn't need self, we can make it a static method
    @staticmethod
    def print_details(new_name, new_age):
        print(f"{new_name}'s age is {new_age}.")


rahul = Friend("rahul", 20)
rohit = Friend("rohit", 22)

rohit.print

# can be called from an object like -
rohit.print_details("Ram", 32)

# and also like this - (don't need any object)
Friend.print_details("Ram", 32)
