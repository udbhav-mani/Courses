import sqlite3

from utils.Encrypt import Encrypt
from utils.db_context_manager import DBconnect
import hashlib


class Database:

    @staticmethod
    def is_valid_login(username, password):
        with DBconnect() as cursor:
            cursor.execute("SELECT password,role FROM login where username = ?", (username,))
            output = cursor.fetchall()
            if len(output):
                db_pass, role = output[0]
            else:
                return False

        encrypt_obj = Encrypt()
        if encrypt_obj.check_password(password, db_pass):
            return True, role
        else:
            return False, None

    @staticmethod
    def add_data(emp):
        with DBconnect() as cursor:
            cursor.execute("INSERT INTO employee (id,name,department,email) VALUES (?,?,?,?)",
                           (emp['id'], emp['name'], emp['department'], emp['email']))

    @staticmethod
    def fetch_data():
        with DBconnect() as cursor:
            cursor.execute("SELECT * from employee")
            emp = [{"id": line[0], "name": line[1], "email": line[2], "department": line[3]}
                   for line in
                   cursor.fetchall()]
        return emp

    @staticmethod
    def delete_data(emp_name):
        with DBconnect() as cursor:
            cursor.execute("DELETE FROM employee where name = ?", (emp_name,))

    @staticmethod
    def search_data(emp_name):
        with DBconnect() as cursor:
            cursor.execute("SELECT * from employee where name = ?", (emp_name,))
            emp = [line for line in cursor.fetchall()]
        return emp

    @staticmethod
    def update_database(emp_data):
        with DBconnect() as cursor:
            cursor.execute("UPDATE employee SET id = ?, email = ?, department = ? WHERE condition = ",
                           (emp_data["id"], emp_data["email"], emp_data["department"]))


if __name__ == "__main__":
    db_object = Database()
    # print(db_object.is_valid_login("Ram", "pass123"))
    db_object.fetch_data()
