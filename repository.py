import json
from typing import List
from models import Book, Patron, Transaction
from pathlib import Path


class LibraryRepository:
    def __init__(self, file_path="library.json"):
        self.file_path = Path(file_path)
        self.books: List[Book] = []
        self.patrons: List[Patron] = []
        self.transactions: List[Transaction] = []

    # -------------------
    # CRUD - BOOKS
    # -------------------
    def add_book(self, book: Book):
        if any(b.id == book.id for b in self.books):
            raise ValueError(f"Book with id {book.id} already exists")
        self.books.append(book)
        self.save()

    def remove_book(self, book_id: int):
        self.books = [b for b in self.books if b.id != book_id]

    def get_book(self, book_id: int):
        return next((b for b in self.books if b.id == book_id), None)

    # -------------------
    # SAVE
    # -------------------
    def save(self):

        data = {
            "books": [b.model_dump() for b in self.books],
            "patrons": [p.model_dump() for p in self.patrons],
            "transactions": [t.model_dump() for t in self.transactions],
        }

        self.file_path.write_text(json.dumps(data, indent=2, default=str))

    # -------------------
    # LOAD
    # -------------------
    def load(self):
        if not self.file_path.exists():
            return

        content = self.file_path.read_text().strip()

        if not content:
            return

        data = json.loads(content)

        self.books = [Book.model_validate(b) for b in data["books"]]
        self.patrons = [Patron.model_validate(p) for p in data["patrons"]]
        self.transactions = [Transaction.model_validate(t) for t in data["transactions"]]

    def add_patron(self, patron):
        self.patrons.append(patron)

    def get_patron(self, patron_id):
        return next((p for p in self.patrons if p.id == patron_id), None)

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def get_transaction(self, transaction_id):
        return next((t for t in self.transactions if t.id == transaction_id), None)