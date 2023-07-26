from Database import Database
from search_employee import search_emp


db_obj = Database()


def employee_details(name):
    index = search_emp(name)
    if index == -1:
        return

    empData = db_obj.fetch_data()

    print(f"Name : {empData['employee'][index]['name']}")
    print(f"ID : {empData['employee'][index]['id']}")
    print(f"Department : {empData['employee'][index]['department']}")
    print(f"Email : {empData['employee'][index]['email']}")

    modify_details(empData, index)


def modify_details(emp_data, index):
    print("Enter the Details To Update, Leave Blank if not required : ")

    name = input("Enter Name : ").strip()
    id = input("Enter ID : ").strip()
    department = input("Enter Department : ").strip()
    email = input("Enter Email : ").strip()
    if name != "":
        emp_data["employee"][index]["name"] = name
    if id != "":
        emp_data["employee"][index]["id"] = id
    if department != "":
        emp_data["employee"][index]["department"] = department
    if email != "":
        emp_data["employee"][index]["email"] = email

    db_obj.update_database(emp_data)
