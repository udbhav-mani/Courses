from fastapi import Body, FastAPI

app = FastAPI()

BOOKS = [
    {"title": "Harry Potter", "author": "J. K. Rowling", "category": "Fantasy"},
    {
        "title": "Jurassic Park",
        "author": "Michael Crichton",
        "category": "Science Fiction",
    },
    {"title": "The Martian", "author": "Andy Weir", "category": "Science Fiction"},
    {"title": "The Da Vinci Code", "author": "Dan Brown", "category": "Thriller"},
    {
        "title": "The Fellowship of the Ring",
        "author": "J. R. R. Tolkien",
        "category": "Fantasy",
    },
    {
        "title": "A Game of Thrones",
        "author": "George R. R. Martin",
        "category": "Fantasy",
    },
]


@app.get("/")
async def getapi():
    return dict(message="hello world")


@app.get("/books")
async def get_all_books():
    return BOOKS


@app.get("/books/{book_name}")
async def get_a_book(book_name: str):
    for book in BOOKS:
        if book.get("title").casefold() == book_name.casefold():
            return book


@app.get("/books/")
async def get_books_by_category(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get("category").casefold() == category.casefold():
            books_to_return.append(book)

    return books_to_return


@app.get("/books/{book_title}")
async def get_books_by_category(book_title: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if (
            book.get("title").casefold() == book_title.casefold()
            and book.get("category").casefold() == category.casefold()
        ):
            books_to_return.append(book)

    return books_to_return


@app.get("/books/byauthor/{author}")
async def get_books_by_category(author: str):
    books_to_return = []
    for book in BOOKS:
        if book.get("author").casefold() == author.casefold():
            books_to_return.append(book)

    return books_to_return


@app.post("/create-book")
def add_book(new_book=Body()):
    BOOKS.append(new_book)


@app.put("/update-book")
def add_book(new_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i]["title"].casefold() == new_book["title"].casefold():
            BOOKS[i] = new_book
            break


@app.put("/delete-book/{book_title}")
def add_book(book_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i]["title"].casefold() == book_title.casefold():
            BOOKS.pop(i)
            break
