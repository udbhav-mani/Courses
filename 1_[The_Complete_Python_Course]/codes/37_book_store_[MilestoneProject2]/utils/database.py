books = []


def add_book(book_name, book_author):
    books.append({"name": book_name, "author": book_author, "read": False})


def read_book(book_name):
    for book in books:
        if book["name"] == book_name:
            book["read"] = True
            break


def list_book():
    return books


def delete_book(book_name):
    for index, book in enumerate(books, start=0):
        if book["name"] == book_name:
            del books[index]
            break
