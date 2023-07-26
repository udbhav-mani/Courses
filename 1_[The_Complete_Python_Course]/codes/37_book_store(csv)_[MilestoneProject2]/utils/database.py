books_filename = "books.csv"


def add_book(book_name, book_author):
    with open(books_filename, "a") as file:
        book = f"{book_name},{book_author},{False}\n"
        file.write(book)


def list_book():
    with open(books_filename, "r") as file:
        books = file.readlines()

    books = [book.strip().split(",") for book in books]
    return [{"name": book[0], "author": book[1], "read": book[2]} for book in books]


def _save_books(books):
    with open(books_filename, "w") as file:
        for book in books:
            file.write(f"{book['name']},{book['author']},{book['read']}\n")


def read_book(book_name):
    books = list_book()
    for index, book in enumerate(books, start=0):
        if book["name"] == book_name:
            book["read"] = True
            break
    _save_books(books)


def delete_book(book_name):
    books = list_book()
    new_books = [book for book in books if book["name"] != book_name]
    _save_books(new_books)
