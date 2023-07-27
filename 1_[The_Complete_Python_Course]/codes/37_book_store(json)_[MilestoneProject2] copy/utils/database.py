from utils.database_connect import DatabaseConnect

books_filename = "books.json"


def create_new_booktable():
    with DatabaseConnect("data.db") as cursor:
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer)"
        )


def add_book(book_name, book_author):
    with DatabaseConnect("data.db") as cursor:
        cursor.execute("INSERT INTO books VALUES(?,?,?)", (book_name, book_author, 0))


def list_book():
    with DatabaseConnect("data.db") as cursor:
        cursor.execute("SELECT * FROM BOOKS")
        books = [
            {
                "name": line[0],
                "author": line[1],
                "read": line[2],
            }
            for line in cursor.fetchall()
        ]
    return books


def read_book(book_name):
    with DatabaseConnect("data.db") as cursor:
        cursor.execute("UPDATE books SET read = 1 WHERE name = ?", (book_name,))


def delete_book(book_name):
    with DatabaseConnect("data.db") as cursor:
        cursor.execute("DELETE FROM books WHERE name = ?", (book_name,))
