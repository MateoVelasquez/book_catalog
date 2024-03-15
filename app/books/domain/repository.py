"""
Repository

Interface that defines the operations that can be performed with books.
These operations are encapsulated within an abstract class (a class that cannot
be instantiated directly but serves as a template for the following operations).
"""

from abc import abstractmethod, ABC
from typing import List, Optional

from .entity import Book


class BookRepositoryAbstract(ABC):

    @abstractmethod
    def get_all_books(self) -> List[Book]:
        """
        Retrieves all books from the repository.

        Returns:
            List[Book]: A list of all books stored in the repository.
        """
        raise NotImplementedError

    @abstractmethod
    def get_by_isbn(self, isbn: str) -> Optional[Book]:
        """
        Retrieves a book from the repository by its ISBN.

        Args:
            isbn (str): The ISBN of the book to retrieve.

        Returns:
            Optional[Book]: The book object if found, None otherwise.
        """
        raise NotImplementedError

    @abstractmethod
    def create_book(self, book: Book) -> Book:
        """
        Creates a new book in the repository.

        Args:
            book (Book): The book object to be created.

        Returns:
            Book: The newly created book object.
        """
        raise NotImplementedError

    @abstractmethod
    def delete_book(self, book_id: str) -> Optional[Book]:
        """
        Deletes a book from the repository by its ID.

        Args:
            book_id (str): The ID of the book to delete.

        Returns:
            Optional[Book]: Book or None
        """
        raise NotImplementedError

    @abstractmethod
    def update_book(self, book_id: str, new_book_data: Book) -> Optional[Book]:
        """
        Updates the information of a book in the repository.

        Args:
            new_book_data (Book): The updated book object.

        Returns:
            Optional[Book]: The updated book object if successful, None otherwise.
        """
        raise NotImplementedError
