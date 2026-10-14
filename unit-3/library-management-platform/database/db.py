import threading

# Lock protects shared in-memory data.
_lock = threading.RLock()

books = {
    1: {
        "id": 1,
        "title": "Python Programming",
        "author": "Guido van Rossum",
        "available": True,
    },
    2: {
        "id": 2,
        "title": "Clean Code",
        "author": "Robert C. Martin",
        "available": True,
    },
    3: {
        "id": 3,
        "title": "Introduction to Algorithms",
        "author": "Thomas H. Cormen",
        "available": True,
    },
}

users = {
    1: {"id": 1, "name": "Admin User", "role": "admin"},
    2: {"id": 2, "name": "Student User", "role": "user"},
}

loans = {}

_next_book_id = 4
_next_user_id = 3
_next_loan_id = 1


def reset_data():
    """Reset the in-memory data to its initial state."""
    global books, users, loans
    global _next_book_id, _next_user_id, _next_loan_id

    with _lock:
        books = {
            1: {
                "id": 1,
                "title": "Python Programming",
                "author": "Guido van Rossum",
                "available": True,
            },
            2: {
                "id": 2,
                "title": "Clean Code",
                "author": "Robert C. Martin",
                "available": True,
            },
            3: {
                "id": 3,
                "title": "Introduction to Algorithms",
                "author": "Thomas H. Cormen",
                "available": True,
            },
        }
        users = {
            1: {"id": 1, "name": "Admin User", "role": "admin"},
            2: {"id": 2, "name": "Student User", "role": "user"},
        }
        loans = {}
        _next_book_id = 4
        _next_user_id = 3
        _next_loan_id = 1


def get_lock():
    """Return the lock used for synchronized data operations."""
    return _lock
