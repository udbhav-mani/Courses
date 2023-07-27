import json
from Database import Database


class Employee:
    def __init__(self, employee_id, employee_name, employee_email, employee_department):
        self.id = employee_id
        self.name = employee_name
        self.email = employee_email
        self.department = employee_department


