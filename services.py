from datetime import date, timedelta
from models import Transaction, Book
from repository import LibraryRepository


class LibraryService:
    def __init__(self, repo: LibraryRepository):
        self.repo = repo

    def checkout_book(self, book_id: int, patron_id: int):
        book = self.repo.get_book(book_id)

        if not book or book.available_copies <= 0:
            raise ValueError("Book not available")

        book.available_copies -= 1

        transaction = Transaction(
            id=len(self.repo.transactions) + 1,
            book_id=book_id,
            patron_id=patron_id,
            checkout_date=date.today(),
            due_date=date.today() + timedelta(days=14),
        )

        self.repo.transactions.append(transaction)
        return transaction

    def return_book(self, transaction_id: int):
        transaction = next(
            (t for t in self.repo.transactions if t.id == transaction_id),
            None
        )

        if not transaction:
            raise ValueError("Transaction not found")

        transaction.return_date = date.today()

        book = self.repo.get_book(transaction.book_id)
        if book:
            book.available_copies += 1

        return transaction.calculate_late_fee()