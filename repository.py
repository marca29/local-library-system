import json
from typing import List
from models import Book, Patron, Transaction


class LibraryRepository:
    def __init__(self, file_path="library.json"):
        self.file_path = file_path
        self.books: List[Book] = []
        self.patrons: List[Patron] = []
        self.transactions: List[Transaction] = []

    # -------------------
    # CRUD - BOOKS
    # -------------------
    def add_book(self, book: Book):
        self.books.append(book)

    def remove_book(self, book_id: int):
        self.books = [b for b in self.books if b.id != book_id]

    def get_book(self, book_id: int):
        return next((b for b in self.books if b.id == book_id), None)

    def add_patron(self, patron):
        self.patrons.append(patron)

    def get_patron(self, patron_id):
        return next((p for p in self.patrons if p.id == patron_id), None)

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def get_transaction(self, transaction_id):
        return next((t for t in self.transactions if t.id == transaction_id), None)