import os
import mysql.connector

from src.helpers.exceptions import DbException
from environs import Env

env = Env()
env.read_env(path="src/.env")


class Database:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB"),
        )
        self.cursor = self.connection.cursor()

    def add_item(self, query, data):
        try:
            self.cursor.execute(query, data)
            _id = self.cursor.lastrowid
            self.connection.commit()

        except Exception:
            raise DbException()
        else:
            return _id

    def add_items(self, query, data):
        try:
            self.cursor.executemany(query, data)
            _id = self.cursor.lastrowid
            self.connection.commit()
        except Exception:
            raise DbException
        else:
            return _id

    def get_item(self, query, data=None):
        try:
            self.cursor.execute(query, data)
            response = self.cursor.fetchone()
        except Exception:
            raise DbException
        else:
            return response

    def get_items(self, query, data):
        try:
            self.cursor.execute(query, data)
            response = self.cursor.fetchall()
            self.connection.commit()
        except Exception:
            raise DbException
        else:
            return response

    def update_item(self, query, data):
        try:
            self.cursor.execute(query, data)
            _id = self.cursor.lastrowid
            self.connection.commit()
        except Exception:
            raise DbException
        else:
            return _id


db = Database()
