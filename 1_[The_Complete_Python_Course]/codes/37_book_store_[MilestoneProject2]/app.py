from utils import database

USER_CHOICE = """
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit

Your choice: """


def menu():
    user_input = input(USER_CHOICE)

    while user_input != "q":
        user_validations[user_input]()
        user_input = input(USER_CHOICE)


def prompt_add_book():
    book_name = input("Enter book name : ")
    book_author = input("Enter author's name : ")

    book = {"name": book_name, "author": book_author, "read": False}
    database.add_book(book)


def prompt_read_book():
    book_name = input("Enter the name of the book you have read: ")
    database.read_book(book_name)


def list_book():
    database.list_book()


def prompt_delete_book():
    book_name = input("Enter book name to be deleted : ")
    database.delete_book(book_name)


user_validations = {
    "a": prompt_add_book,
    "l": list_book,
    "r": prompt_read_book,
    "d": prompt_delete_book,
}


if __name__ == "__main__":
    menu()
