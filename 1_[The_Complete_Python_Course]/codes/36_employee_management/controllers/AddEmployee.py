import json
from Employee import Employee
from Database import Database


class AddEmployee(Employee):
    def add_emp(self):
        emp = {
            "name": self.name,
            "id": self.id,
            "email": self.email,
            "department": self.department,
        }

        database = Database()
        data = database.fetch_data()
        data["employee"].append(emp)
        database.update_database(data)
