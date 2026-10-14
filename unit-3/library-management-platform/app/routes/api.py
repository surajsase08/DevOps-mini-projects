
from flask import Blueprint, jsonify, request
from app.services import library_service

api = Blueprint("api", __name__)


@api.route("/books", methods=["GET"])
def list_books():
    return jsonify(library_service.get_books()), 200


@api.route("/books/<int:book_id>", methods=["GET"])
def get_book(book_id):
    book = library_service.get_book(book_id)

    if book is None:
        return jsonify({"error": "Book not found."}), 404

    return jsonify(book), 200


@api.route("/books", methods=["POST"])
def create_book():
    data = request.get_json(silent=True)

    if data is None:
        return jsonify({
            "error": "A JSON request body is required."
        }), 400

    book, error = library_service.add_book(data)

    if error:
        return jsonify({"error": error}), 400

    return jsonify(book), 201


@api.route("/users", methods=["GET"])
def list_users():
    return jsonify(library_service.get_users()), 200


@api.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = library_service.get_user(user_id)

    if user is None:
        return jsonify({"error": "User not found."}), 404

    return jsonify(user), 200


@api.route("/users", methods=["POST"])
def create_user():
    data = request.get_json(silent=True)

    if data is None:
        return jsonify({
            "error": "A JSON request body is required."
        }), 400

    user, error = library_service.add_user(data)

    if error:
        return jsonify({"error": error}), 400

    return jsonify(user), 201


@api.route("/borrow", methods=["POST"])
def borrow_book():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({
            "error": "A JSON request body is required."
        }), 400

    try:
        book_id = int(data["book_id"])
        user_id = int(data["user_id"])
    except (KeyError, TypeError, ValueError):
        return jsonify({
            "error": "Valid book_id and user_id are required."
        }), 400

    loan, error = library_service.borrow_book(book_id, user_id)

    if error:
        not_found = ("Book not found.", "User not found.")
        status = 404 if error in not_found else 409
        return jsonify({"error": error}), status

    return jsonify(loan), 201


@api.route("/return", methods=["POST"])
def return_book():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({
            "error": "A JSON request body is required."
        }), 400

    try:
        book_id = int(data["book_id"])
        user_id = int(data["user_id"])
    except (KeyError, TypeError, ValueError):
        return jsonify({
            "error": "Valid book_id and user_id are required."
        }), 400

    success, error = library_service.return_book(book_id, user_id)

    if not success:
        status = 404 if error == "Book not found." else 409
        return jsonify({"error": error}), status

    return jsonify({
        "message": "Book returned successfully."
    }), 200


@api.route("/loans", methods=["GET"])
def list_loans():
    return jsonify(library_service.get_loans()), 200
