import json
from Database import Database


def delete_employee(emp_name):
    database = Database()
    data = database.fetch_data()

    for index, emp in enumerate(data["employee"], start=0):
        if emp["name"].lower() == emp_name.lower():
            del data["employee"][index]

    database.update_database(data)
