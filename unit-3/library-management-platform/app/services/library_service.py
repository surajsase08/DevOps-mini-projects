from database import db
from app.models.book import Book
from app.models.user import User


def get_books():
    with db.get_lock():
        return [dict(book) for book in db.books.values()]


def get_book(book_id):
    with db.get_lock():
        book = db.books.get(book_id)
        return dict(book) if book else None


def add_book(data):
    valid, error = Book.validate(data)
    if not valid:
        return None, error

    with db.get_lock():
        book_id = db._next_book_id
        db._next_book_id += 1

        book = {
            "id": book_id,
            "title": data["title"].strip(),
            "author": data["author"].strip(),
            "available": True,
        }
        db.books[book_id] = book
        return dict(book), None


def get_users():
    with db.get_lock():
        return [dict(user) for user in db.users.values()]


def get_user(user_id):
    with db.get_lock():
        user = db.users.get(user_id)
        return dict(user) if user else None


def add_user(data):
    valid, error = User.validate(data)
    if not valid:
        return None, error

    with db.get_lock():
        user_id = db._next_user_id
        db._next_user_id += 1

        user = {
            "id": user_id,
            "name": data["name"].strip(),
            "role": data.get("role", "user"),
        }
        db.users[user_id] = user
        return dict(user), None


def borrow_book(book_id, user_id):
    with db.get_lock():
        book = db.books.get(book_id)
        user = db.users.get(user_id)

        if not book:
            return None, "Book not found."
        if not user:
            return None, "User not found."
        if not book["available"]:
            return None, "Book is already borrowed."

        loan_id = db._next_loan_id
        db._next_loan_id += 1

        loan = {
            "id": loan_id,
            "book_id": book_id,
            "user_id": user_id,
            "returned": False,
        }
        db.loans[loan_id] = loan
        book["available"] = False

        return dict(loan), None


def return_book(book_id, user_id):
    with db.get_lock():
        book = db.books.get(book_id)
        if not book:
            return False, "Book not found."

        for loan in db.loans.values():
            if (
                loan["book_id"] == book_id
                and loan["user_id"] == user_id
                and not loan["returned"]
            ):
                loan["returned"] = True
                book["available"] = True
                return True, None

        return False, "No active loan found for this user and book."


def get_loans():
    with db.get_lock():
        return [dict(loan) for loan in db.loans.values()]
