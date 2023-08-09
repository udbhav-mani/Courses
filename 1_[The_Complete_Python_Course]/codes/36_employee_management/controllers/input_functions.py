from controllers.AddEmployee import AddEmployee
from controllers.DeleteEmployee import DeleteEmployee
from controllers.ViewEmployee import ViewEmployee
from controllers.SearchEmployee import SearchEmployee
from controllers.ModifyEmployee import ModifyEmployee


def add_emp_input():
    user_name = input("Enter employee name - ")
    user_id = input("Enter employee id - ")
    user_email = input("Enter employee email - ")
    user_department = input("Enter employee department - ")

    emp = AddEmployee(user_id, user_name, user_email, user_department)
    emp.add_emp()

    print(f"{user_name.title()} is added! Thank You ")


def search_emp_input():
    user_input = input("Which employee do you want to search for ? ")
    search_emp_obj = SearchEmployee()
    search_emp_obj.search_emp(user_input)


def view_emp_input():
    view_emp_obj = ViewEmployee()
    view_emp_obj.view_emp()


def delete_emp_input():
    user_input = input("Which employee do you want to delete ? ")
    del_emp_object = DeleteEmployee()
    del_emp_object.delete_employee(user_input)


def modify_emp_input():
    user_input = input("Which employee do you want to modify ? ")
    modify_emp_obj = ModifyEmployee()
    modify_emp_obj.employee_details(user_input)
