class Salary:
    # def __init__(self):
    #     print(self.__class__)
    #     # print(cls.__class__)

    # define Salary class and associated methods here
    # @classmethod
    def calculate(cls, hours):
        # print("salary - ", cls.__class__)
        return cls.rate * hours


class Promotable:
    def promote(cls, increase):
        print("promotable - ", cls.__class__)
        cls.rate += increase


# Do NOT change the code below:
class Employee(Salary, Promotable):
    def __init__(self, rate: float):
        # super().__init__(self)
        self.rate = rate

    def weekly_salary(self) -> float:
        return self.calculate(40)


emp = Employee(15.0)
print(emp.calculate(40))
salary = Salary()
print(isinstance(emp, Salary))

print(emp.weekly_salary())
