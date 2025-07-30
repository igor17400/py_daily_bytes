###############
# Day 3: Descriptors
###############

"""
Goal:
Create a reusable "Validator" that automatically ensures an attribute (like an email address) on
an object is always a valid format when set, and raise an error if it's not.
"""

###############
# Approach using @property decorator
###############

class UserProperty:
    def __init__(self, username, email):
        self._username = username
        self.email = email  # calls the setter

    @property
    def username(self):
        return self._username

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if not isinstance(value, str) or '@' not in value or '.' not in value:
            raise ValueError("Email address is not valid")
        self._email = value

    def __repr__(self):
        return f"UserProperty(username='{self.username}', email='{self.email}')"

if __name__ == "__main__":
    print("--- Traditional Approach (using @property) ---")
    try:
        user1 = UserProperty("alice", "alice@example.com")
        print(f"Created: {user1}")
        user1.email = "new.alice@domain.co"
        print(f"Updated: {user1}")

        # This will raise an error
        user2 = UserProperty("bob", "invalid-email")
        print(f"Created: {user2}")  # This line won't be reached
    except ValueError as e:
        print(f"Error caught: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    print("\n--- Another attempt with invalid email ---")
    try:
        user3 = UserProperty("charlie", "charlie@web")  # Missing dot
    except ValueError as e:
        print(f"Error caught: {e}")

