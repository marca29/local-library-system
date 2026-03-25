# Library Management System

A simple library management system written in Python. The application runs in the command line (CLI) and allows you to manage books, borrowing, and returns.

## Features

* Add books
* Borrow books
* Return books (with late fee calculation)
* Data validation (ISBN, email, dates)
* Save and load data from a JSON file

## Project Structure

```
.
├── cli.py              # Command-line interface
├── models.py           # Data models (Book, Patron, Transaction)
├── repository.py       # Data access layer (JSON storage)
├── services.py         # Business logic
├── requirements.txt    # Dependencies
├── test_*.py           # Unit tests
```

## Requirements

* Python 3.10+
* Libraries:

  * pydantic

Install dependencies:

```
pip install -r requirements.txt
```

## Running the Application

```
python cli.py
```

## Application Menu

After running, you’ll see options like:

1. Add a book
2. Borrow a book
3. Return a book
4. Save and exit

## How It Works

### Book Model

* Validates ISBN
* Ensures available copies do not exceed total copies

### Patron Model

* Validates email addresses

### Transaction Model

* Represents a borrowing record
* Automatically calculates late fees (1 unit per day)

### Repository

* Stores data in `library.json`
* Handles saving and loading data

### Service Layer

* Contains business logic:

  * borrowing books
  * returning books
  * calculating fees

## Late Fees

* 1 day late = 1 unit fee
* No fee if returned on time

## Possible Improvements

* User authentication (login system)
* GUI (e.g., Tkinter or web app)
* Borrowing history
* Book search functionality
* REST API (e.g., FastAPI)

## Authors

**Marcelina Górka**
**Michalina Górka**
