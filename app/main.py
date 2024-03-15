"""
Main Module

This module serves as the entry point for the FastAPI application. It configures the FastAPI
application instance, registers routers, and defines exception handlers for handling domain-specific
errors.

Features:
- Configures the FastAPI application with title, description, and version.
- Registers routers for different endpoints.
- Defines exception handlers for handling domain-specific errors.

Note:
    This file should be executed to start the FastAPI application.

"""

from fastapi import FastAPI
from dotenv import find_dotenv, load_dotenv

from app.books.infraestructure.api.api_routers import books_router
from app.error_handlers import register_error_handlers

# Load dotenv:
load_dotenv(find_dotenv('.env'))

# APP definition
app = FastAPI(
    title="Books Catalog",
    description=
    "REST API with FastAPI and MongoDB using Ports and Adapters architecture (Hexagonal)",
    version="0.0.1")

# Routers
app.include_router(books_router)

# Error handlers
register_error_handlers(app)
