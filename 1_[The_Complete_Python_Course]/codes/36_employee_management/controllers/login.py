from views.admin import menu as adm_menu
from views.employee import menu as emp_menu
from utils.Database import Database
import maskpass
from utils.Validators import Validators

redirects = {"admin": adm_menu, "employee": emp_menu}


USER_CHOICE = """
Employee Management System"""


def validate_login(username, password):
    dbobject = Database()
    is_validated = dbobject.is_valid_login(username, password)
    if is_validated:
        return Database.get_role(username=username)
    else:
        return None


def login():
    username = input("Enter username -> ")
    while not Validators.validate_name(username):
        username = input("Please enter a valid username - ")
    password = input("Enter password -> ")

    # password = maskpass.advpass(prompt="Enter password -> ")
    # print(password)

    role = validate_login(username, password)

    if role is not None:
        redirects[role]()
    else:
        print("Wrong credentials, Please Try again!!")
        login()


if __name__ == "__main__":
    print(USER_CHOICE)
    login()
