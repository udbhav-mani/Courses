import sqlite3

from utils.Encrypt import Encrypt
from utils.db_context_manager import DBconnect
import hashlib


class Database:

    @staticmethod
    def is_valid_login(username, password):
        with DBconnect() as cursor:
            cursor.execute("SELECT password FROM login where username = ?", (username,))
            output = cursor.fetchall()
            if len(output):
                db_pass = output[0]
            else:
                return False

        encrypt_obj = Encrypt()
        if encrypt_obj.check_password(password, db_pass[0]):
            return True
        else:
            return False

    @staticmethod
    def get_role(username):
        with DBconnect() as cursor:
            cursor.execute("SELECT role from login where username = ?", (username,))
            emp_role = [{"emp_role": line[0]} for line in cursor.fetchall()]

            return emp_role[0]['emp_role']

    @staticmethod
    def add_data(emp):
        try:
            with DBconnect() as cursor:
                cursor.execute("INSERT INTO employee (id,name,department,email) VALUES (?,?,?,?)",
                               (emp['id'], emp['name'], emp['department'], emp['email']))
                return "success"
        except:
            return "fail"

    @staticmethod
    def fetch_data():
        with DBconnect() as cursor:
            cursor.execute("SELECT * from employee")
            emp = [{"id": line[0], "name": line[1], "email": line[3], "department": line[2]}
                   for line in
                   cursor.fetchall()]
        return emp

    @staticmethod
    def delete_data(emp_name):
        if len(Database.search_data(emp_name.title())) == 0:
            return f"No employee named {emp_name}."
        else:
            with DBconnect() as cursor:
                cursor.execute("DELETE from employee where name = ?", (emp_name.title(),))
                return f"{emp_name} deleted successfully!"

    @staticmethod
    def search_data(emp_name):
        with DBconnect() as cursor:
            cursor.execute("SELECT * from employee where name = ?", (emp_name,))
            emp = [{"id": line[0], "name": line[1], "email": line[3], "department": line[2]}
                   for line in cursor.fetchall()]
        return emp

    @staticmethod
    def update_database(emp_data):
        with DBconnect() as cursor:
            cursor.execute("UPDATE employee SET id = ?, email = ?, department = ? WHERE name = ?",
                           (emp_data["id"], emp_data["email"], emp_data["department"], emp_data["name"]))


if __name__ == "__main__":
    db_object = Database()
    # print(db_object.is_valid_login("Ram", "pass123"))
    # db_object.get_role("Ram")
    db_object.fetch_data()
