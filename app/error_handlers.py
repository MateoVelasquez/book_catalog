"""
Error Handlers

This module defines error handlers for handling domain-specific exceptions in the FastAPI application.

Functions:
    - register_error_handlers(app): Registers exception handlers for ResourceNotFound and ConflictError exceptions.
"""
from typing import Callable
from fastapi import HTTPException
from fastapi.requests import Request

from app.books.domain.exceptions import ResourceNotFound, ConflictError


def handle_exception(status_code: int) -> Callable:
    """
    Decorator function to create exception handlers for different status codes.

    Args:
        status_code (int): The HTTP status code to be raised.

    Returns:
        Callable: The exception handler function.

    """

    def decorator(func):

        def wrapper(request: Request, exc):
            _ = request
            raise HTTPException(status_code, str(exc))

        return wrapper

    return decorator


def register_error_handlers(app):
    """
    Registers exception handlers for ResourceNotFound and ConflictError exceptions.

    Args:
        app: The FastAPI application instance.

    """

    @app.exception_handler(ResourceNotFound)
    @handle_exception(404)
    def resource_not_found_handler(request: Request, exc: ResourceNotFound):
        """
        Exception handler for ResourceNotFound errors.

        Args:
            request (Request): The request object.
            exc (ResourceNotFound): The ResourceNotFound exception object.

        Raises:
            HTTPException: HTTP exception with status code 404.

        """
        pass

    @app.exception_handler(ConflictError)
    @handle_exception(409)
    def conflict_error_handler(request: Request, exc: ResourceNotFound):
        """
        Exception handler for ConflictError errors.

        Args:
            request (Request): The request object.
            exc (ConflictError): The ConflictError exception object.

        Raises:
            HTTPException: HTTP exception with status code 409.

        """
        pass
