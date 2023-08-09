from utils.Database import Database
from controllers.SearchEmployee import SearchEmployee
from Employee import Employee

db_obj = Database()


class ModifyEmployee(Employee):
    def __init__(self):
        pass

    def employee_details(self, name):
        emp_data = db_obj.search_data(emp_name=name)
        if len(emp_data) == 0:
            return

        print(f"Name : {emp_data['name']}")
        print(f"ID : {emp_data['id']}")
        print(f"Department : {emp_data['department']}")
        print(f"Email : {emp_data['email']}")

        self.modify_details(emp_data)

    @staticmethod
    def modify_details(emp_data):
        print("Enter the Details To Update, Leave Blank if not required : ")

        emp_id = input("Enter ID : ").strip()
        department = input("Enter Department : ").strip()
        email = input("Enter Email : ").strip()

        if emp_id != "":
            emp_data["id"] = emp_id
        if department != "":
            emp_data["department"] = department
        if email != "":
            emp_data["email"] = email

        db_obj.update_database(emp_data)


if __name__ == "__main__":
    obj = ModifyEmployee()
    obj.modify_details("rohna")
