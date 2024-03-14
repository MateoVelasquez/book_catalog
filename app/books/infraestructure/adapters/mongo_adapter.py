"""
MongoDB Adapter

Provides an implementation of the book repository using MongoDB as the data storage.
"""
from typing import List, Optional
from bson import ObjectId
from pymongo.database import Database
from pymongo.collection import Collection

from app.books.domain.entity import Book
from app.books.domain.repository import BookRepositoryAbstract


class MongoDBAdapter(BookRepositoryAbstract):

    def __init__(self, database: Database) -> None:
        """
        Initializes the MongoDBAdapter with a specific MongoDB database.

        Args:
            database (Database): The MongoDB database to use.
        """
        self.collection: Collection = database.get_collection('books')

    def get_all_books(self) -> List[Book]:
        """
        Retrieves all books from the database.

        Returns:
            List[Book]: A list of all books stored in the database.
        """
        return list(self.collection.find())

    def get_by_isbn(self, isbn: str) -> Optional[Book]:
        """
        Retrieves a book from the database by its ISBN.

        Args:
            isbn (str): The ISBN of the book to retrieve.

        Returns:
            Optional[Book]: The book object if found, None otherwise.
        """
        book_data = self.collection.find_one({'isbn': isbn})
        if book_data:
            return book_data
        else:
            return None

    def create_book(self, book: Book) -> Book:
        """
        Creates a new book in the database.

        Args:
            book (Book): The book object to be created.

        Returns:
            Book: The newly created book object.
        """
        inserted_id = self.collection.insert_one(book.model_dump()).inserted_id
        book.id = str(inserted_id)
        return book

    def update_book(self, book_id: str, new_book_data: Book) -> Optional[Book]:
        """
        Updates the information of a book in the database.

        Args:
            book_id (str): The ID of the book to update.
            new_book_data (Book): The updated book object.

        Returns:
            Optional[Book]: The updated book object if successful, None otherwise.
        """
        updated_book = self.collection.find_one_and_update(
            {"_id": ObjectId(book_id)}, {"$set": new_book_data.dict()})
        if updated_book:
            return self.collection.find_one({"_id": ObjectId(book_id)})
        else:
            return None

    def delete_book(self, book_id: str) -> Optional[Book]:
        """
        Deletes a book from the database by its ID.

        Args:
            book_id (str): The ID of the book to delete.

        Returns:
            Optional[Book]: The deleted book object if successful, None otherwise.
        """
        deleted_book = self.collection.find_one_and_delete({"_id": ObjectId(book_id)})
        if deleted_book:
            return deleted_book
        else:
            return None
