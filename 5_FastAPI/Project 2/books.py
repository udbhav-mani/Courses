from fastapi import FastAPI, Path, Query, HTTPException, Body
from pydantic import BaseModel, Field
from typing import Optional
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


BOOKS = [
    Book(1, "Computer Science Pro", "codingwithroby", "A very nice book!", 5, 2030),
    Book(2, "Be Fast with FastAPI", "codingwithroby", "A great book!", 5, 2030),
    Book(3, "Master Endpoints", "codingwithroby", "A awesome book!", 5, 2029),
    Book(4, "HP1", "Author 1", "Book Description", 2, 2028),
    Book(5, "HP2", "Author 2", "Book Description", 3, 2027),
    Book(6, "HP3", "Author 3", "Book Description", 1, 2026),
]


class BookRequest(BaseModel):
    id: Optional[int] = Field(title="id not needed.")
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=3, maxlength=200)
    rating: int = Field(gt=0, lt=6)
    published_date: int = Field(gt=1999, lt=2031)

    class Config:
        json_schema_extra = {
            "example": {
                "title": "A new book",
                "author": "codingwithroby",
                "description": "A new description of a book",
                "rating": 5,
                "published_date": 2029,
            }
        }


@app.get("/books")
def get_all_books():
    return BOOKS


@app.get(
    "/books/{book_id}",
    status_code=status.HTTP_200_OK,
)
def get_book_by_id(book_id: int):
    for book in BOOKS:
        if book.id == book_id:
            return book
    return 
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")


@app.post("/books")
def post_book(body: BookRequest):
    new_book = Book(**body.model_dump())
    BOOKS.append(get_book_id(new_book))


@app.get("/books/")
def get_books_by_rating(rating: int):
    book_list = []
    for book in BOOKS:
        if book.rating == rating:
            book_list.append(book)

    return book_list


@app.put("/books/update")
def update_book(body: BookRequest):
    for i in range(len(BOOKS)):
        if BOOKS[i].id == body.id:
            new_book = Book(**body.model_dump())
            BOOKS[i] = new_book


def get_book_id(book):
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    return book
