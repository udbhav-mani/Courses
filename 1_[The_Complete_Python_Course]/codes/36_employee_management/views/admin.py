import controllers.input_functions as input_functions

user_validations = {
    "1": input_functions.add_emp_input,
    "2": input_functions.search_emp_input,
    "3": input_functions.view_emp_input,
    "4": input_functions.delete_emp_input,
    "5": input_functions.modify_emp_input,
}

CHOICES_TEXT = """1) Add Employee
2) Search an Employee
3) View All Employees
4) Delete an employee
5) Modify an employee
6) Exit
"""


def menu():
    print("Hello welcome to WatchGuard!! Choose from the options below - ")
    while True:

        try:
            user_input = input(CHOICES_TEXT+"Your Choice - ")
            if user_input == "6":
                print("\nThank You ! Have a nice day :) ")
                break
            else:
                user_validations[user_input]()
        except KeyError:
            print("\nInvalid Input, Please choose between (1-6)! ")
        else:
            user_choice = input("Want to do something else? (y/n) ")
            while user_choice != "y":
                if user_choice == "n":
                    break
                else:
                    user_choice = input("Wrong Input! Please try again! (y/n) ")
            if user_choice == "n":
                print("Thank You ! Have a nice day :) ")
                break


if __name__ == "__main__":
    menu()
