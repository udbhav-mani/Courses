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

    def __str__(self):
        return f"Name - {self.name}, age - {self.age}."

    def __repr__(self):
        return f"Name - {self.name}, age - {self.age}."

    @classmethod
    def class_print(cls):
        print(cls)


class BestFriend(Friend):
    def __init__(self, name, age, time):
        super().__init__(name, age)
        self.time = time

    def __str__(self):
        return f"Name - {self.name}, age - {self.age}, time - {self.time}."


rahul = Friend("rahul", 20)
rohit = Friend("rohit", 22)
raj = BestFriend("raj", 23, 15)

# rohit.print

# and also like this - (don't need any object)
# Friend.print_details("Ram", 32)

# # rohit's print using __str__
print(rohit)
# # raj's print using __str__
raj.class_print()
