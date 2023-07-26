import json
from Database import Database


def search_emp(name):
    db_object = Database()
    data = db_object.fetch_data()

    for index, employee in enumerate(data["employee"]):
        if employee["name"] == name:
            return index
    else:
        return -1
