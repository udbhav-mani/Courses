from utils.Database import Database
from Employee import Employee


class SearchEmployee(Employee):
    def __init__(self):
        pass

    @staticmethod
    def search_emp(name):
        db_object = Database()
        length = len(db_object.search_data(emp_name=name.title()))
        if length > 0:
            print(f"{name.title()} is an employee of WatchGuard!")
        else:
            print(f"{name} is not an employee of WatchGuard!")
