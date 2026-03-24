
import unittest
from datetime import date, timedelta
from pydantic import ValidationError

from models import Book, Patron, Transaction


class TestModels(unittest.TestCase):

    # -------------------
    # BOOK
    # -------------------
    def test_create_book_success(self):
        book = Book(
            id=1,
            title="Test",
            author="Author",
            isbn="9781234567897",
            total_copies=5,
            available_copies=3
        )
        self.assertEqual(book.title, "Test")

    def test_invalid_isbn(self):
        with self.assertRaises(ValidationError):
            Book(
                id=1,
                title="Test",
                author="Author",
                isbn="INVALID",
                total_copies=5,
                available_copies=3
            )

    def test_available_exceeds_total(self):
        with self.assertRaises(ValidationError):
            Book(
                id=1,
                title="Test",
                author="Author",
                isbn="9781234567897",
                total_copies=2,
                available_copies=5
            )

    # -------------------
    # PATRON
    # -------------------
    def test_valid_email(self):
        patron = Patron(id=1, name="Jan", email="jan@test.com")
        self.assertEqual(patron.email, "jan@test.com")

    def test_invalid_email(self):
        with self.assertRaises(ValidationError):
            Patron(id=1, name="Jan", email="bad-email")

    # -------------------
    # TRANSACTION
    # -------------------
    def test_due_date_validation(self):
        with self.assertRaises(ValidationError):
            Transaction(
                id=1,
                book_id=1,
                patron_id=1,
                checkout_date=date.today(),
                due_date=date.today()  # invalid
            )

    def test_late_fee_calculation(self):
        t = Transaction(
            id=1,
            book_id=1,
            patron_id=1,
            checkout_date=date.today() - timedelta(days=20),
            due_date=date.today() - timedelta(days=10),
            return_date=date.today()
        )

        fee = t.calculate_late_fee()
        self.assertGreater(fee, 0)

    def test_no_late_fee(self):
        t = Transaction(
            id=1,
            book_id=1,
            patron_id=1,
            checkout_date=date.today(),
            due_date=date.today() + timedelta(days=5),
            return_date=date.today()
        )

        self.assertEqual(t.calculate_late_fee(), 0.0)


if __name__ == "__main__":
    unittest.main()