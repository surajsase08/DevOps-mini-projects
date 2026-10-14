class User:
    """Represents a user of the library."""

    VALID_ROLES = {"admin", "user"}

    def __init__(self, user_id, name, role="user"):
        self.id = user_id
        self.name = name
        self.role = role

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "role": self.role,
        }

    @staticmethod
    def validate(data):
        if not isinstance(data, dict):
            return False, "User data must be an object."

        if not isinstance(data.get("name"), str) or not data["name"].strip():
            return False, "Name is required."

        role = data.get("role", "user")
        if role not in User.VALID_ROLES:
            return False, "Role must be admin or user."

        return True, None
