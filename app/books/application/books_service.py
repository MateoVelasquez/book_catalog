"""
Books Service

This module defines the business logic for managing books within the application. The service orchestrates
the interaction between the domain entities and the repository adapters, implementing various operations
such as retrieval, creation, updating, and deletion of books.

Classes:
    - BookService: Implements the business logic for managing books.

"""

from typing import List

from ..domain.entity import Book
from ..domain.exceptions import BookNotFoundException, BookAlreadyExistsException
from ..domain.repository import BookRepositoryAbstract


class BookService:

    def __init__(self, book_repository: BookRepositoryAbstract) -> None:
        """
        Initializes the BookService with a specific BookRepository.

        Args:
            book_repository (BookRepositoryAbstract): The repository used for book data operations.
        """
        self.book_repository = book_repository

    def get_all_books(self) -> List[Book]:
        """
        Retrieves all books from the repository.

        Returns:
            List[Book]: A list of all books stored in the repository.
        """
        return self.book_repository.get_all_books()

    def get_book_by_isbn(self, isbn: str) -> Book:
        """
        Retrieves a book from the repository by its ISBN.

        Args:
            isbn (str): The ISBN of the book to retrieve.

        Returns:
            Book: The book object if found.

        Raises:
            BookNotFoundException: If the book with the given ISBN is not found.
        """
        book = self.book_repository.get_by_isbn(isbn)
        if not book:
            raise BookNotFoundException(f"Book with ISBN {isbn} not found.")
        return book

    def create_book(self, book: Book) -> Book:
        """
        Creates a new book in the repository.

        Args:
            book (Book): The book object to be created.

        Returns:
            Book: The newly created book object.

        Raises:
            BookAlreadyExistsException: If a book with the same ISBN already exists.
        """
        registered_book = self.book_repository.get_by_isbn(book.isbn)
        if registered_book:
            raise BookAlreadyExistsException(
                f"Book with ISBN {book.isbn} already exists.")
        created_book = self.book_repository.create_book(book)
        return created_book

    def delete_book(self, book_id: str) -> None:
        """
        Deletes a book from the repository.

        Args:
            book_id (str): The ID of the book to delete.

        Raises:
            BookNotFoundException: If the book with the given ID is not found.
        """
        deleted_book = self.book_repository.delete_book(book_id)
        if not deleted_book:
            raise BookNotFoundException(f"Book with ID {book_id} not found.")

    def update_book(self, book_id: str, book_data: Book) -> Book:
        """
        Updates the information of a book in the repository.

        Args:
            book_id (str): The ID of the book to update.
            book_data (Book): The updated book data.

        Returns:
            Book: The updated book object.

        Raises:
            BookNotFoundException: If the book with the given ID is not found.
        """
        updated_book = self.book_repository.update_book(book_id, book_data)
        if not updated_book:
            raise BookNotFoundException(f"Book with ID {book_id} not found.")
        return updated_book
