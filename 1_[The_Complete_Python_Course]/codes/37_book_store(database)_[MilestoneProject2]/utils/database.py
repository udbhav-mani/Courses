import json

books_filename = "books.json"


# def create_newfile():
#     with open(books_filename, "w") as file:
#         json.dump([], file)


def add_book(book_name, book_author):
    books = list_book()
    books.append({"name": book_name, "author": book_author, "read": False})
    _save_books(books)


def list_book():
    with open(books_filename, "r") as file:
        return json.load(file)


def _save_books(books):
    with open(books_filename, "w") as file:
        json.dump(books, file, indent=2)


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
