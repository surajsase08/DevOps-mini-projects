
import pytest
from app import create_app
from database import db


@pytest.fixture
def client():
    db.reset_data()
    app = create_app()
    app.config["TESTING"] = True

    with app.test_client() as test_client:
        yield test_client


def test_home_endpoint(client):
    response = client.get("/")

    assert response.status_code == 200
    assert response.json["status"] == "running"


def test_health_endpoint(client):
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json["status"] == "healthy"


def test_list_books_endpoint(client):
    response = client.get("/api/books")

    assert response.status_code == 200
    assert len(response.json) == 3


def test_create_book_endpoint(client):
    response = client.post(
        "/api/books",
        json={
            "title": "DevOps Fundamentals",
            "author": "Test Author",
        },
    )

    assert response.status_code == 201
    assert response.json["title"] == "DevOps Fundamentals"


def test_book_not_found_endpoint(client):
    response = client.get("/api/books/999")

    assert response.status_code == 404
    assert response.json["error"] == "Book not found."
