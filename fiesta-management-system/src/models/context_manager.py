import mysql.connector


class DatabaseConnection:
    def __init__(self):
        self.db_connector = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Password3#",
            database="fiesta_management_system",
        )
        self.cursor = self.db_connector.cursor()

    def __enter__(self):
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.db_connector.commit()
        self.db_connector.close()
