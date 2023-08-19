class Student:
    def __init__(self, name, address, grades):
        self.name = name
        self.address = address
        self.grades = grades

    def avg(self):
        return sum(self.grades) / len(self.grades)

    def __repr__(self):
        return f"{self.grades}"


student1 = Student("abc", "def", [12, 23, 34])
student2 = Student("ghi", "jkl", range(96, 99))
print(student1.avg())
print(student2.avg())
print(
    student1
)  # the repr class will represent the object otherwise it will not be of string type
