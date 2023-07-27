import json
from Database import Database
from Employee import Employee


class DeleteEmployee(Employee):
    def __init__(self):
        pass

    def delete_employee(self, emp_name):
        db_object = Database()
        data = db_object.fetch_data()

        for index, emp in enumerate(data["employee"], start=0):
            if emp["name"].lower() == emp_name.lower():
                del data["employee"][index]

        db_object.update_database(data)
