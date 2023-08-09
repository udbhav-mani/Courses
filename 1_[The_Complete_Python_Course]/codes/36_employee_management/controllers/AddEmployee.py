from Employee import Employee
from utils.Database import Database


class AddEmployee(Employee):
    def add_emp(self):
        emp = {
            "name": self.name,
            "id": self.id,
            "email": self.email,
            "department": self.department,
        }

        database = Database()
        data = database.add_data(emp)
        print("Employee added succesfully !! ")
