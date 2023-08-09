import controllers.input_functions as input_functions

user_validations = {
    "1": input_functions.add_emp_input,
    "2": input_functions.search_emp_input,
    "3": input_functions.view_emp_input,
}

CHOICES_TEXT = """1) Add Employee
2) Search an Employee
3) View All Employees
4) Exit
"""


def menu():
    print("Hello welcome to WatchGuard!! Choose from the options below - ")

    while True:

        try:
            user_input = input(CHOICES_TEXT+"Your Choice - ")
            if user_input == "4":
                print("\nThank You ! Have a nice day :) ")
                break
            else:
                user_validations[user_input]()
        except KeyError:
            print("\nInvalid Input, Please choose between (1-4)! ")
        else:
            user_choice = input("Want to do something else? (y/n) ")
            if user_choice == "n":
                print("\nThank You ! Have a nice day :) ")
                break


if __name__ == "__main__":
    menu()
