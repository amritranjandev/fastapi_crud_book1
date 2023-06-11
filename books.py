from enum import Enum
from typing import List, Optional,Union

from fastapi import FastAPI

app = FastAPI()

BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'}
]


class DirectionName(str, Enum):
    """
    Enumeration of direction names.

    Each direction name represents a specific direction.

    Possible values:
        - north: North direction.
        - south: South direction.
        - east: East direction.
        - west: West direction.
    """
    north = "North"
    south = "South"
    east = "East"
    west = "West"


@app.get('/')
async def read_all_books(skip_book: Optional[str] = None) -> List[dict]:
    """
    Retrieve all books.

    If `skip_book` is provided, exclude the book with the matching title.

    Args:
        skip_book (str, optional): The title of the book to skip. Defaults to None.

    Returns:
        List[dict]: List of books.
    """
    new_books = BOOKS.copy()
    if skip_book:
        new_books = [book for book in new_books if book['title'] != skip_book]
    return new_books


@app.post('/')
async def create_book(book_title: str, book_author: str, category: str) -> List[dict]:
    """
    Create a new book.

    Args:
        book_title (str): The title of the book.
        book_author (str): The author of the book.
        category (str): The category of the book.

    Returns:
        List[dict]: List of books.
    """
    BOOKS.append({'title': book_title, 'author': book_author, 'category': category})
    return BOOKS


@app.put('/{title}')
async def update_book(title: str, book_author: str, category: str) -> List[dict]:
    """
    Update an existing book.

    Args:
        title (str): The title of the book to update.
        book_author (str): The updated author of the book.
        category (str): The updated category of the book.

    Returns:
        List[dict]: List of books.
    """
    for book in BOOKS:
        if book['title'] == title:
            book['author'] = book_author
            book['category'] = category
            return BOOKS
    return BOOKS


@app.delete('/{title}')
async def delete_book(title: str) -> List[dict]:
    """
    Delete a book.

    Args:
        title (str): The title of the book to delete.

    Returns:
        List[dict]: List of books.
    """
    BOOKS[:] = [book for book in BOOKS if book['title'] != title]
    return BOOKS


@app.get('/assignment/')
async def read_book_assignment(title: str) -> Union[dict, str]:
    """
    Retrieve a book by title.

    Args:
        title (str): The title of the book to retrieve.

    Returns:
        Union[dict, str]: The book as a dictionary if found, otherwise an error message.
    """
    for book in BOOKS:
        if book['title'] == title:
            return book
