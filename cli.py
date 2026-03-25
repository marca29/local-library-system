from repository import LibraryRepository
from services import LibraryService
from models import Book

repo = LibraryRepository()
repo.load()
service = LibraryService(repo)


def main():
    while True:
        print("\n--- Library Menu ---")
        print("1. Add Book")
        print("2. Checkout Book")
        print("3. Return Book")
        print("4. Save & Exit")

        choice = input("Select: ")

        if choice == "1":
            book = Book(
                id=int(input("ID: ")),
                title=input("Title: "),
                author=input("Author: "),
                isbn=input("ISBN: "),
                total_copies=int(input("Total Copies: ")),
                available_copies=int(input("Available Copies: "))
            )

            repo.add_book(book)
            repo.save() 
            print("Book added & saved!")

        elif choice == "2":
            service.checkout_book(
                int(input("Book ID: ")),
                int(input("Patron ID: "))
            )

            repo.save() 
            print("Book checked out & saved!")

        elif choice == "3":
            fee = service.return_book(int(input("Transaction ID: ")))

            repo.save() 
            print(f"Returned. Late fee: {fee}")

        elif choice == "4":
            repo.save()
            print("Data saved. Goodbye!")
            break


if __name__ == "__main__":
    main()