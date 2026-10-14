
from app.services import library_service
from database import db


def test_get_books_returns_seeded_books():
    db.reset_data()

    books = library_service.get_books()

    assert len(books) == 3
    assert books[0]["title"] == "Python Programming"


def test_add_book_successfully():
    db.reset_data()

    book, error = library_service.add_book({
        "title": "DevOps Fundamentals",
        "author": "Test Author",
    })

    assert error is None
    assert book["title"] == "DevOps Fundamentals"
    assert book["available"] is True


def test_add_book_rejects_missing_title():
    db.reset_data()

    book, error = library_service.add_book({
        "title": "",
        "author": "Test Author",
    })

    assert book is None
    assert error == "Title is required."
