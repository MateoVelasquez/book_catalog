"""
Custom Exceptions for Domain Errors:

This module defines custom exceptions to handle domain-specific errors within the application. 
These exceptions provide a way to handle different types of errors that may occur during 
the execution of the application's business logic.

Exceptions:
    DomainError: Base class for domain-specific exceptions.
    ResourceNotFound: Exception raised when a requested resource is not found.
    ConflictError: Exception raised when there is a conflict with the current state of the resource.

Custom Exceptions for Book Domain:

This module defines custom exceptions related to the book domain within the application. 
These exceptions provide specific error handling for operations involving books, such as 
creating or retrieving books from the repository.

Exceptions:
    BookNotFoundException: Exception raised when a book is not found in the repository.
    BookAlreadyExistsException: Exception raised when trying to create a book that already
    exists in the repository.
"""

class DomainError(Exception):
    """
    Base class for domain-specific exceptions.
    """
    pass


class ResourceNotFound(DomainError):
    """
    Exception raised when a requested resource is not found.
    """
    pass


class ConflictError(DomainError):
    """
    Exception raised when there is a conflict with the current state of the resource.
    """
    pass


class BookNotFoundException(ResourceNotFound):
    """
    Exception raised when a book is not found in the repository.
    """
    pass


class BookAlreadyExistsException(ConflictError):
    """
    Exception raised when trying to create a book that already exists in the repository.
    """
    pass
