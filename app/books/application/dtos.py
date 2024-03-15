"""
DTO Module

This module defines Data Transfer Objects (DTOs) used for
transferring data between different layers of the application.
"""
from typing import Optional, Annotated
from pydantic import BaseModel, Field, BeforeValidator


class BookDTO(BaseModel):
    id: Optional[Annotated[str, BeforeValidator(str)]] = Field(None,
                                                               alias='_id')
    isbn: str = Field(
        ...,
        title=
        "The ISBN of the book (unique identifier). Must be a 13-digit code.",
        max_length=17,
        min_length=17)
    author: str = Field(..., title="The author of the book.")
    title: str = Field(..., title="The title of the book.")
    description: str = Field("", title="The description of the book.")
