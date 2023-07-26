from Employee import Employee
from delete_employee import delete_employee
from search_employee import search_emp
import view_employee
import modify_employee


def add_emp_input():
    user_name = input("Enter employee name - ")
    user_id = input("Enter employee id - ")
    user_email = input("Enter employee email - ")
    user_department = input("Enter employee department - ")

    emp = Employee(user_id, user_name, user_email, user_department)
    emp.add_emp()

    print(f"{user_name.title()} is added! Thank You ")


def search_emp_input():
    user_input = input("Which employee do you want to search for ? ")
    index = search_emp(user_input)
    if index != -1:
        print(f"{user_input.title()} is an employee of the organization of WatchGuard")
    else:
        print(
            f"{user_input.title()} is not an employee of the organization of WatchGuard"
        )


def view_emp_input():
    view_employee.view_emp()


def delete_emp_input():
    user_input = input("Which employee do you want to delete ? ")
    delete_employee(user_input)


def modify_emp_input():
    user_input = input("Which employee do you want to modify ? ")
    modify_employee.employee_details(user_input)
