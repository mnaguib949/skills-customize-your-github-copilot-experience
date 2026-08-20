"""Starter code for the Building REST APIs with FastAPI assignment."""

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Book Catalog API")

books = [
    {"id": 1, "title": "A Wrinkle in Time", "author": "Madeleine L'Engle"},
    {"id": 2, "title": "The Giver", "author": "Lois Lowry"},
]


class BookCreate(BaseModel):
    """Fields required when a client creates a book."""

    title: str
    author: str


@app.get("/health")
def health_check():
    """Confirm that the API is running."""
    pass


@app.get("/books")
def list_books():
    """Return every book in the catalog."""
    pass


@app.get("/books/{book_id}")
def get_book(book_id: int):
    """Return one book by ID."""
    pass


@app.post("/books", status_code=201)
def create_book(book: BookCreate):
    """Add a new book to the catalog."""
    pass


@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    """Delete one book by ID."""
    pass
