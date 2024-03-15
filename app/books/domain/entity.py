"""Entities

Defines the basic properties of the entities in the application.
The representation of objects that will be managed in the system.


Note: You don't need to define the __init__ method when using @dataclass,
as this is done automatically.
You can omit it and let dataclass handle initialization for you.
This will simplify your code.
"""
from dataclasses import dataclass


@dataclass
class Book:
    """
    Represents a book in the system.

    Attributes:

        isbn (str): The ISBN of the book (unique identifier). Must be a
            13-digit code.
        title (str): The title of the book. Cannot be empty.
        author (str): The author of the book. Cannot be empty.
        description (str): The description of the book. Can be empty.

    Examples:

        >>> book = Book(isbn="978-1-4920-5809-4", title="The Little Prince", author="Antoine de Saint-Exupéry")
        >>> book.isbn
        '978-1-4920-5809-4'
        >>> book.title
        'The Little Prince'

    """
    id: str
    isbn: str
    author: str
    title: str
    description: str = ""
