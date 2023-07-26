import json


class AddEmployee:
    def __init__(self, employee):
        self.name = employee.employee_name
        self.id = employee.employee_id
        self.email = employee.employee_email
        self.department = employee.employee_department
        self.add_emp()

    