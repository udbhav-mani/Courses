from app import book


def print_sorted_books():
    best_books = sorted(book, key=lambda x: x.get_rating * -1)[:5]
    for i in best_books:
        print(i)

def print_cheap_books():
    best_books = sorted(book, key=lambda x: x.get_price)[:5]
    for i in best_books:
        print(i)


print_cheap_books()
