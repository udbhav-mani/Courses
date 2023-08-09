import sqlite3


class DBconnect:
    filename = r"C:\Users\umani\Desktop\projects\Employee_management\utils\data.db"

    def __init__(self):
        pass

    def __enter__(self):
        self.connection = sqlite3.connect(self.filename)
        cursor = self.connection.cursor()

        return cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.commit()
        self.connection.close()
