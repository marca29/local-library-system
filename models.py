
from pydantic import BaseModel, Field, field_validator
from datetime import date, datetime
from typing import ClassVar
import re


# -------------------
# BOOK MODEL
# -------------------
class Book(BaseModel):
    id: int
    title: str
    author: str
    isbn: str
    total_copies: int = Field(gt=0)
    available_copies: int = Field(ge=0)

    @field_validator("isbn")
    def validate_isbn(cls, v):
        pattern = r"^(97(8|9))?\d{9}(\d|X)$"
        if not re.match(pattern, v):
            raise ValueError("Invalid ISBN format")
        return v

    @field_validator("available_copies")
    def check_available_not_exceed_total(cls, v, info):
        if "total_copies" in info.data and v > info.data["total_copies"]:
            raise ValueError("Available copies cannot exceed total copies")
        return v


# -------------------
# PATRON MODEL
# -------------------
class Patron(BaseModel):
    id: int
    name: str
    email: str

    @field_validator("email")
    def validate_email(cls, v):
        if "@" not in v:
            raise ValueError("Invalid email")
        return v


# -------------------
# TRANSACTION MODEL
# -------------------
class Transaction(BaseModel):
    id: int
    book_id: int
    patron_id: int
    checkout_date: date
    due_date: date
    return_date: date | None = None

    @field_validator("due_date")
    def validate_due_date(cls, v, values):
        if "checkout_date" in values and v <= values["checkout_date"]:
            raise ValueError("Due date must be after checkout")
        return v

    def calculate_late_fee(self):
        if not self.return_date or self.return_date <= self.due_date:
            return 0.0
        days = (self.return_date - self.due_date).days
        return days * 1.0