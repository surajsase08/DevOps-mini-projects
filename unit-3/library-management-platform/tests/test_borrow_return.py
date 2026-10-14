
from app.services import library_service
from database import db


def test_borrow_book_successfully():
    db.reset_data()

    loan, error = library_service.borrow_book(book_id=1, user_id=2)

    assert error is None
    assert loan["book_id"] == 1
    assert loan["user_id"] == 2
    assert db.books[1]["available"] is False


def test_cannot_borrow_already_borrowed_book():
    db.reset_data()

    library_service.borrow_book(book_id=1, user_id=2)
    loan, error = library_service.borrow_book(book_id=1, user_id=1)

    assert loan is None
    assert error == "Book is already borrowed."


def test_return_book_successfully():
    db.reset_data()

    library_service.borrow_book(book_id=1, user_id=2)
    success, error = library_service.return_book(book_id=1, user_id=2)

    assert success is True
    assert error is None
    assert db.books[1]["available"] is True


def test_cannot_return_book_without_active_loan():
    db.reset_data()

    success, error = library_service.return_book(book_id=1, user_id=2)

    assert success is False
    assert error == "No active loan found for this user and book."
