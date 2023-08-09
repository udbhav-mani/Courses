from utils.Database import Database
from Employee import Employee


class DeleteEmployee(Employee):
    def __init__(self):
        pass

    @staticmethod
    def delete_employee(emp_name):
        db_object = Database()
        data = db_object.delete_data(emp_name)
        print(f"{emp_name} deleted successfully!")
