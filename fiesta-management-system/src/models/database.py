import os

import mysql.connector
from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path("src/utils/.env")

load_dotenv(dotenv_path=dotenv_path)
HOST = os.getenv("HOST")
print(HOST)


class Database:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Password3#",
            database="fiesta_management_system",
        )
        self.cursor = self.connection.cursor()

    def add_item(self, query, data):
        self.cursor.execute(query, data)
        _id = self.cursor.lastrowid
        self.connection.commit()
        return _id

    def add_items(self, query, data):
        self.cursor.executemany(query, data)
        _id = self.cursor.lastrowid
        self.connection.commit()
        return _id

    def get_item(self, query, data=None):
        self.cursor.execute(query, data)
        response = self.cursor.fetchone()
        return response

    def get_items(self, query, data=None):
        self.cursor.execute(query, data)
        response = self.cursor.fetchall()
        return response

    def update_item(self, query, data):
        self.cursor.execute(query, data)
        _id = self.cursor.lastrowid
        self.connection.commit()
        return _id
