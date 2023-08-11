from utils.Database import Database
from Employee import Employee


class ViewEmployee(Employee):
    def __init__(self):
        pass

    @staticmethod
    def view_emp():
        database = Database()
        contents = database.fetch_data()

        print("Employee Database : ")

        for i, emp in enumerate(contents, start=1):
            print(f"\nEmployee {i} Data : ")
            print(f"ID : {emp['id']}")
            print(f"Name : {emp['name']}")
            print(f"Department : {emp['department']}")
            print(f"Email : {emp['email']}")

    @staticmethod
    def view_emp_names():
        database = Database()
        contents = database.fetch_data()

        for i, emp in enumerate(contents, start=1):
            print(f"Employee {i} Name: {emp['name']} ")