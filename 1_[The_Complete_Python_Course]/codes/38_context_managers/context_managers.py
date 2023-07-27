# we have to make both entry and exit functions like

import sqlite3


class DBconnect:
    def __init__(self, filename) -> None:
        self.connection = None
        self.filename = filename

    # during with time
    def __enter__(self):
        self.connection = sqlite3.connect(self.filename)
        return self.connection

    # during exit time
    def __exit__(self, exc_val, exc_type, exc_tb):
        if exc_val or exc_type or exc_tb:
            self.connection.commit()
            self.connection.close()
