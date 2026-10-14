
class Book:
    """Represents a book in the library."""

    def __init__(self, book_id, title, author, available=True):
        self.id = book_id
        self.title = title
        self.author = author
        self.available = available

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "available": self.available,
        }

    @staticmethod
    def validate(data):
        if not isinstance(data, dict):
            return False, "Book data must be an object."

        title = data.get("title")
        if not isinstance(title, str) or not title.strip():
            return False, "Title is required."

        author = data.get("author")
        if not isinstance(author, str) or not author.strip():
            return False, "Author is required."

        return True, None
