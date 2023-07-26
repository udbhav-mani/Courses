import input_functions


user_validations = {
    "1": input_functions.add_emp_input,
    "2": input_functions.search_emp_input,
    "3": input_functions.view_emp_input,
    "4": input_functions.delete_emp_input,
    "5": input_functions.modify_emp_input,
}


def menu():
    while True:
        print("Hello welcome to WatchGuard!! Choose from the options below - ")
        print("1) Add Employee")
        print("2) Search an Employee")
        print("3) View All Employees")
        print("4) Delete an employee")
        print("5) Modify an employee")

        user_input = input("Your Choice - ")
        user_validations[user_input]()

        user_choice = input("Want to do something else? (y/n)")
        if user_choice == "n":
            break


if __name__ == "__main__":
    menu()
