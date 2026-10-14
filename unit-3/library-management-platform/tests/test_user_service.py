
from app.services import library_service
from database import db


def test_get_users_returns_seeded_users():
    db.reset_data()

    users = library_service.get_users()

    assert len(users) == 2
    assert users[0]["name"] == "Admin User"
    assert users[1]["name"] == "Student User"


def test_add_user_successfully():
    db.reset_data()

    user, error = library_service.add_user({
        "name": "New Student",
        "role": "user",
    })

    assert error is None
    assert user["name"] == "New Student"
    assert user["role"] == "user"


def test_add_user_rejects_invalid_role():
    db.reset_data()

    user, error = library_service.add_user({
        "name": "New Student",
        "role": "superadmin",
    })

    assert user is None
    assert error == "Role must be admin or user."
