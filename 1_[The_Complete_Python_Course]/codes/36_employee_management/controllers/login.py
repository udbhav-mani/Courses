from views.admin import menu as adm_menu
from views.employee import menu as emp_menu
from utils.Database import Database

redirects = {
    "admin": adm_menu,
    "employee": emp_menu
}


USER_CHOICE = """
Employee Management System"""

def validate_login(username, password):
    dbobject = Database()
    validation, role = dbobject.is_valid_login(username, password)
    if validation:
        return role
    else:
        return None


def login():
    print(USER_CHOICE)
    username = input("Enter username -> ")
    password = input("Enter password -> ")
    role = validate_login(username, password)

    if role is not None:
        redirects[role]()
    else:
        print("Wrong credentials!!")


if __name__ == "__main__":
    login()
