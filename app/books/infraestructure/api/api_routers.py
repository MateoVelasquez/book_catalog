"""
API Routers

Defines the endpoints for manipulating books in the API.
"""
from fastapi import APIRouter, Depends
from typing import List
from starlette import status

from app.database import db_manager

from ...application.dtos import BookDTO
from ...application.books_service import BookService
from ..adapters.mongo_adapter import MongoDBAdapter

books_router = APIRouter(tags=['books'])


def get_adapter() -> BookService:
    return BookService(MongoDBAdapter(db_manager.get_database()))


@books_router.get('/books', response_model=List[BookDTO])
def get_books(service: BookService = Depends(get_adapter)):
    return service.get_all_books()


@books_router.get('/books/{isbn}', response_model=BookDTO)
def get_book_by_isbn(isbn: str, service: BookService = Depends(get_adapter)):
    book = service.get_book_by_isbn(isbn)
    return book


@books_router.post('/books', response_model=BookDTO)
def new_book(book: BookDTO, service: BookService = Depends(get_adapter)):
    return service.create_book(book)


@books_router.put('/books/{book_id}', response_model=BookDTO)
def update_book(book_id: str,
                book_data: BookDTO,
                service: BookService = Depends(get_adapter)):
    return service.update_book(book_id, book_data)


@books_router.delete('/books/{book_id}',
                     status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: str, service: BookService = Depends(get_adapter)):
    service.delete_book(book_id)
