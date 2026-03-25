import unittest
from repository import LibraryRepository
from services import LibraryService
from models import Book


class TestServices(unittest.TestCase):

    def setUp(self):
        self.repo = LibraryRepository()

        self.repo.add_book(
            Book(
                id=1,
                title="Clean Code",
                author="Robert C. Martin",
                isbn="9780132350884",
                total_copies=3,
                available_copies=3
            )
        )

        self.service = LibraryService(self.repo)

    # -------------------
    # CHECKOUT TEST
    # -------------------
    def test_checkout_reduces_stock(self):
        self.service.checkout_book(1, 100)

        self.assertEqual(self.repo.books[0].available_copies, 2)
        self.assertEqual(len(self.repo.transactions), 1)

    # -------------------
    # RETURN TEST
    # -------------------
    def test_return_increases_stock(self):
        self.service.checkout_book(1, 100)
        fee = self.service.return_book(1)

        self.assertEqual(self.repo.books[0].available_copies, 3)
        self.assertIsInstance(fee, float)

    # -------------------
    # ERROR TEST
    # -------------------
    def test_checkout_unavailable_book(self):
        self.repo.books[0].available_copies = 0

        with self.assertRaises(ValueError):
            self.service.checkout_book(1, 100)


if __name__ == "__main__":
    unittest.main()