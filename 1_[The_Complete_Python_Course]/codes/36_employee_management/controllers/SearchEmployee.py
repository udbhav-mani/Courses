import json
from Database import Database
from Employee import Employee


class SearchEmployee(Employee):
    def __init__(self):
        pass

    def search_emp(self, name):
        db_object = Database()
        data = db_object.fetch_data()

        for index, employee in enumerate(data["employee"]):
            if employee["name"] == name:
                return index
        else:
            return -1
