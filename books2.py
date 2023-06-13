from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel,Field
from uuid import UUID
app=FastAPI()

class Book(BaseModel):
    id:UUID
    title:str=Field(min_length=1)
    author:str=Field(min_length=1,max_length=100)
    description:Optional[str]=Field(title="Description of the book",max_length=100,min_length=1)
    rating:int=Field(gt=-1,lt=101)

    class Config:
        schema_extra={
            'example':{
                'id':'3fa85f64-5717-4562-b3fc-2c963f66afa6',
                'title':'a new book',
                'author':'ar',
                'description':'A sample book desc',
                'rating':80
            }
        }

BOOKS=[]

@app.get('/')
async def read_all_books(books_to_return:Optional[int]=None):
    if not BOOKS:
        create_books_no_api()

    if books_to_return and len(BOOKS)>=books_to_return>0:
        i=1
        new_books=[]
        while i<=books_to_return:
            new_books.append(BOOKS[i-1])
            i+=1
        return new_books
    return BOOKS

@app.get('/book/{book_id}')
async def read_book(book_id:UUID):
    for x in BOOKS:
        if x.id==book_id:
            return x
    return f'{book_id} does not exist'

@app.post("/")
async def create_book(book:Book):
    BOOKS.append(book)
    return book


@app.put('/{book_id}')
async def update_book(book_id:UUID,book:Book):
    counter=0
    for x in BOOKS:
        counter+=1
        if x.id==book_id:
            BOOKS[counter-1]=book
            return BOOKS[counter-1]
    return f'{book_id} does not exist'

@app.delete('/{book_id}')
async def delete_book(book_id:UUID):
    counter=0
    for x in BOOKS:
        counter+=1
        if x.id==book_id:
            del BOOKS[counter-1]
            return f'ID:{book_id} deleted'
    return f'{book_id} does not exist'

def create_books_no_api():
    book1=Book(id='3fa85f64-5717-4562-b3fc-2c963f66afa6',
               title='Title 1',
               author='Author 1',
               description='Description 1',
               rating=60)
    
    book2=Book(id='4fa85f64-5717-4562-b3fc-2c963f66afa6',
               title='Title 2',
               author='Author 2',
               description='Description 2',
               rating=70)
    
    book3=Book(id='5fa85f64-5717-4562-b3fc-2c963f66afa6',
               title='Title 3',
               author='Author 3',
               description='Description 3',
               rating=80)
    
    book4=Book(id='6fa85f64-5717-4562-b3fc-2c963f66afa6',
               title='Title 4',
               author='Author 4',
               description='Description 4',
               rating=90)
    BOOKS.append(book1)
    BOOKS.append(book2)
    BOOKS.append(book3)
    BOOKS.append(book4)