import json
from Database import Database


def view_emp():
    database = Database()
    contents = database.fetch_data()

    print("Employee Database : ")

    for i, emp in enumerate(contents["employee"], start=1):
        print(f"\nEmployee {i} Data : \n")
        print(f"Name : {emp['name']}")
        print(f"ID : {emp['id']}")
        print(f"Department : {emp['department']}")
        print(f"Email : {emp['email']}")
