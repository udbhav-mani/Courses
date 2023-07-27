import sqlite3


class DatabaseConnect:
    def __init__(self, filename) -> None:
        self.connection = None
        self.cursor = None
        self.filename = filename

    def __enter__(self):
        self.connection = sqlite3.connect(self.filename)
        self.cursor = self.connection.cursor()

        return self.cursor

    def __exit__(self, exc_val, exc_type, exc_tb):
        self.connection.commit()
        self.connection.close()
