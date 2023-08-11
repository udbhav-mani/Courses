from utils.Database import Database
from utils.Validators import Validators
from Employee import Employee

db_obj = Database()


class ModifyEmployee(Employee):
    def __init__(self):
        pass

    @staticmethod
    def modify_employee(name):
        employee_data = db_obj.search_data(emp_name=name.title())
        if len(employee_data) == 0:
            return f"No employee named {name} found."

        emp_data = employee_data[0]
        # print(emp_data)
        #
        # print(f"Name : {emp_data['name']}")
        # print(f"ID : {emp_data['id']}")
        # print(f"Department : {emp_data['department']}")
        # print(f"Email : {emp_data['email']}")

        return ModifyEmployee.modify_details(emp_data)

    @staticmethod
    def modify_details(emp_data):
        print("\nEnter the details you want to update, otherwise leave the field blank.")

        emp_id = input(f"Enter new id(current -> {emp_data['id']}): ")
        if emp_id != "":
            while not Validators.validate_id(emp_id):
                emp_id = input("Please enter a valid id - ")
            emp_data["id"] = emp_id

        department = input(f"Enter Department(current -> {emp_data['department']}): ")
        if department != "":
            while not Validators.validate_department(department):
                department = input("Please enter a valid department - ")
            emp_data["department"] = department

        email = input(f"Enter Email(current -> {emp_data['email']}): ")
        if email != "":
            while not Validators.validate_email(email):
                email = input("Please enter a valid email - ")
            emp_data["email"] = email

        db_obj.update_database(emp_data)
        return f"Details Updated Successfully!"


if __name__ == "__main__":
    obj = ModifyEmployee()
    obj.modify_employee("Yash")
