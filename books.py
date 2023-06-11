from fastapi import FastAPI
from enum import Enum
from typing import Optional
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
    north = "North"
    south = "South"
    east = "East"
    west = "West"


# @app.get('/')
# async def read_all_books():
    # return BOOKS

@app.get('/')
async def read_all_books(skip_book: Optional[str] = None):
    new_books = BOOKS.copy()
    if skip_book:
        for each in new_books:
            if each.get('title') == skip_book:
                new_books.remove(each)
    return new_books


# @app.get("/books/mybook")
# async def read_favorite_book():
#     return {"book_title": "My favorite book"}


# @app.get("/books/{book_id}")
# async def read_book(book_id: int):
#     return {"book_title": book_id}

# @app.get("/directions/{direction_name}")
# async def get_direction(direction_name: DirectionName):
#     if direction_name == DirectionName.north:
#         return {"Direction": direction_name, "sub": "Up"}
#     elif direction_name == DirectionName.south:
#         return {"Direction": direction_name, "sub": "Down"}
#     elif direction_name == DirectionName.west:
#         return {"Direction": direction_name, "sub": "Left"}
#     return {"Direction": direction_name, "sub": "Right"}

# @app.get('/{book_name}')
# async def read_book(book_name: str):
#     for each in BOOKS:
#         if each.get('title') == book_name:
#             return each
#     return {book_name: "Not Found"}


@app.post('/')
async def create_book(book_title, book_author, category):
    BOOKS.append(
        {'title': book_title, 'author': book_author, 'category': category})
    return BOOKS


@app.put('/{title}')
async def update_book(title, book_author, category):
    for each in BOOKS:
        if each.get('title') == title:
            each['author'] = book_author
            each['category'] = category
            return BOOKS
    return BOOKS


@app.delete('/{title}')
async def delete_book(title):
    for each in BOOKS:
        if each.get('title') == title:
            BOOKS.remove(each)
    return BOOKS


@app.get('/assignment/')
async def read_book_assignment(title: str):
    for each in BOOKS:
        if each.get('title') == title:
            return each
    return f'title {title} not found'


@app.delete('/assignment/')
async def delete_book_assignment(title: str):
    for each in BOOKS:
        if each.get('title') == title:
            BOOKS.remove(each)
    return BOOKS
