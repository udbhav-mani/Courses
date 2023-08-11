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
        response = database.add_data(emp)
        return response
        # print("Employee added succesfully !! ")
