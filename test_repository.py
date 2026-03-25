import unittest
from unittest.mock import patch, mock_open
from models import Book
from repository import LibraryRepository


class TestRepository(unittest.TestCase):

    def setUp(self):
        self.repo = LibraryRepository("test.json")

    def test_add_book(self):
        book = Book(
            id=1,
            title="Test",
            author="Author",
            isbn="9781234567897",
            total_copies=5,
            available_copies=5
        )
        self.repo.add_book(book)
        self.assertEqual(len(self.repo.books), 1)

    def test_remove_book(self):
        book = Book(
            id=1,
            title="Test",
            author="Author",
            isbn="9781234567897",
            total_copies=5,
            available_copies=5
        )
        self.repo.add_book(book)
        self.repo.remove_book(1)
        self.assertEqual(len(self.repo.books), 0)

    def test_get_book(self):
        book = Book(
            id=1,
            title="Test",
            author="Author",
            isbn="9781234567897",
            total_copies=5,
            available_copies=5
        )
        self.repo.add_book(book)
        found = self.repo.get_book(1)
        self.assertIsNotNone(found)

    # -------------------
    # MOCK FILE SAVE
    # -------------------
    @patch("pathlib.Path.write_text")
    def test_save(self, mock_write):
        self.repo.save()
        mock_write.assert_called_once()

    # -------------------
    # MOCK FILE LOAD
    # -------------------
    @patch("pathlib.Path.exists", return_value=True)
    @patch("pathlib.Path.read_text")
    def test_load(self, mock_read, mock_exists):
        mock_read.return_value = '{"books": [], "patrons": [], "transactions": []}'
        self.repo.load()
        self.assertEqual(len(self.repo.books), 0)


if __name__ == "__main__":
    unittest.main()