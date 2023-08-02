from app import book_objects


def print_best_books():
    best_books = sorted(book_objects, key=lambda x: x.get_rating * -1)[:20]
    for i in best_books:
        print(i)

def print_cheapest_books():
    best_books = sorted(book_objects, key=lambda x: x.get_price)[:5]
    for i in best_books:
        print(i)

next_book = (i for i in book_objects)

def get_next_book():
    print(next(next_book))


USER_CHOICE = '''Enter one of the following

- 'b' to look at 5-star books
- 'c' to look at the cheapest books
- 'n' to just get the next available book on the page
- 'q' to exit

Enter your choice: '''


user_choices = {
    'b': print_best_books,
    'c': print_cheapest_books,
    'n': get_next_book
}


def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input in ('b', 'c', 'n'):
            user_choices[user_input]()
        else:
            print('Please choose a valid command.')
        user_input = input(USER_CHOICE)


menu()