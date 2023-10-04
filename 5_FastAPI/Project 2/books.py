from typing import Optional
from fastapi import Body, FastAPI, Path, Query, HTTPException
from pydantic import BaseModel, Field
from starlette import status

app = FastAPI()


class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int
    published_date: int

    def __init__(self, id, title, author, description, rating, published_date):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_date = published_date


class BookRequest(BaseModel):
    id: Optional[int] = None  # Field(title = "id is not needed")
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=3)
    rating: int = Field(gt=-1, lt=6)
    published_date: int = Field(gt=1900, lt=2024)

    class Config:
        json_schema_extra = {
            "example": {
                "id": 5,
                "title": "Game of Thrones",
                "author": "George R.R. Martin",
                "description": "A song of ice and fire",
                "rating": 5,
                "published_date": 1996,
            }
        }


BOOKS = [
    Book(
        1, "Computer Science Pro", "John Doe", "A book about computer science", 4, 2022
    ),
    Book(
        2,
        "Computer Science for Dummies",
        "Jane Doe",
        "A book about computer science",
        3,
        2008,
    ),
    Book(3, "Fast API Book", "Abhijeet", "A book about Fast API", 5, 2018),
    Book(4, "Python for All", "Abhijeet", "A book about Python", 4, 2022),
]


@app.get("/books", status_code=status.HTTP_200_OK)
async def read_all_books():
    return BOOKS


@app.get("/books/{book_id}", status_code=status.HTTP_200_OK)
async def get_book_by_id(book_id: int = Path(gt=0)):
    for book in BOOKS:
        if book.id == book_id:
            return book

    raise HTTPException(status_code=404, detail="Book Not Found")


@app.get("/books/by_date/", status_code=status.HTTP_200_OK)
async def get_books_by_date(published_date: int = Query(gt=1900, lt=2024)):
    book_list = []

    for book in BOOKS:
        if book.published_date == published_date:
            book_list.append(book)

    return book_list


@app.get("/books/", status_code=status.HTTP_200_OK)
async def get_books_by_rating(rating: int = Query(gt=0, lt=6)):
    books_to_return = []

    for book in BOOKS:
        if book.rating == rating:
            books_to_return.append(book)

    return books_to_return


@app.post("/books/create_book", status_code=status.HTTP_201_CREATED)
async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.model_dump())
    BOOKS.append(find_book_id(new_book))


def find_book_id(book: Book, status_code=status.HTTP_200_OK):
    if len(BOOKS) > 0:
        book.id = BOOKS[-1].id + 1
    else:
        book.id = 1
    return book


@app.put("/books/update_book", status_code=status.HTTP_204_NO_CONTENT)
async def update_book(book: BookRequest):
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id:
            BOOKS[i] = book
    else:
        raise HTTPException(status_code=404, detail="Book Not Found")


@app.delete("/books/delete_book", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int = Query(gt=0)):
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            BOOKS.pop(i)
            break
    else:
        raise HTTPException(status_code=404, detail="Book Not Found")
