from controllers.AddEmployee import AddEmployee
from controllers.DeleteEmployee import DeleteEmployee
from controllers.ViewEmployee import ViewEmployee
from controllers.SearchEmployee import SearchEmployee
from controllers.ModifyEmployee import ModifyEmployee
from utils.Validators import Validators


def add_emp_input():
    user_name = input("Enter employee name - ")
    while not Validators.validate_name(user_name):
        user_name = input("Please enter a name - ")

    user_id = input("Enter employee id - ")
    while not Validators.validate_id(user_id):
        user_id = input("Enter valid id - ")

    user_email = input("Enter employee email - ")
    while not Validators.validate_email(user_email):
        user_email = input("Enter valid email - ")

    user_department = input("Enter employee department - ")
    while not Validators.validate_department(user_department):
        user_department = input("Please enter a department - ")

    emp = AddEmployee(user_id, user_name.title(), user_email, user_department.upper())
    if emp.add_emp() == "success":
        print(f"{user_name.title()} is added! Thank You ")
    else:
        print("ID already present!! Please try again with new ID!")
        add_emp_input()


def search_emp_input():
    user_name = input("Which employee do you want to search for ? ")
    while not Validators.validate_name(user_name):
        user_name = input("Please enter a name - ")

    search_emp_obj = SearchEmployee()
    search_emp_obj.search_emp(user_name)


def view_emp_input():
    view_emp_obj = ViewEmployee()
    view_emp_obj.view_emp()


def delete_emp_input():
    user_name = input("Which employee do you want to delete ? ")
    while not Validators.validate_name(user_name):
        user_name = input("Please enter a name - ")
    del_emp_object = DeleteEmployee()
    del_emp_object.delete_employee(user_name)


def modify_emp_input():
    ViewEmployee.view_emp_names()
    user_name = input("Which employee's details do you want to modify ? ")
    while not Validators.validate_name(user_name):
        user_name = input("Please enter a name - ")
    modify_emp_obj = ModifyEmployee()
    response = modify_emp_obj.modify_employee(user_name)
    print(response)

