###############
# Day 3: Descriptors
###############

"""
Goal:

Create a reusable "Validator" that automatically ensures an attribute (like an email address) on
an object is always a valid format when set, and raise an error if it's not.
"""

###############
# Define a separate class EmailValidator which acts as our descriptor.
# It handles all the validation logic within its __set__ method.
###############

import re


class EmailValidator:
    """
    A custom descriptor to validate email addresses.
    It ensures the assigned value is a string, non-empty,
        and has a basic email structure.
    """

    def __set_name__(self, owner, name):
        # This method is called automatically when the descriptor is assigned toa  class
        # 'owner' is the class (e.g., 'User'), 'name' is the attribute name (e.g., 'email')
        self.public_name = name
        self.private_name = "_" + name  # Where the actual value will be stored (e.g., '_email')

    def __get__(self, obj, objtype=None):
        # Called whe the attribute is accessed (e.g., user.email)
        if obj is None:
            return self  # Accessing descriptor via class (User.email)
        return getattr(obj, self.private_name)

    def __set__(self, obj, value):
        # Called when the attribute is set (e.g., user.email = "test@example.com")
        if not isinstance(value, str):
            raise TypeError(f"'{self.public_name}' must be a string, got {type(value).__name__}")
        if not value.strip():
            raise ValueError(f"'{self.public_name}' cannot be empty.")
        if not re.match(r"[^@]+@[^@]+\.[^@]+", value):  # Simple regex for basic email format
            raise ValueError(f"'{self.public_name}' has an invalid email format: '{value}'")

        setattr(obj, self.private_name, value)  # Store the validate value

    def __delete__(self, obj):
        # Called when the attributed is deleted (e.g., del user.email)
        delattr(obj, self.private_name)


class UserDescriptor:
    """
    A User class that uses our custom EmailValidator descriptor.
    """
    email = EmailValidator()  # Assign the descriptor instance directly

    def __init__(self, username, email):
        self._username = username  # Username managed traditionally
        self.email = email  # This assignment triggers EmailValidator.__set__

    @property
    def username(self):
        return self._username

    def __repr__(self):
        # Accessing self.email here triggers EmailValidator.__get__
        return f"UserDescriptor(username='{self.username}', email='{self.email}')"


## Descriptors are reusable!!
class Company:
    admin_email = EmailValidator()
    contact_email = EmailValidator()

    def __init__(self, name, admin_email, contact_email):
        self.name = name
        self.admin_email = admin_email
        self.contact_email = contact_email

    def __repr__(self):
        return f"Company(name='{self.name}', admin_email='{self.admin_email}', contact_email='{self.contact_email}')"


if __name__ == "__main__":
    print("\n--- The Descriptor Approach ---")
    try:
        user_d1 = UserDescriptor("diana", "diana@example.org")
        print(f"Created: {user_d1}")
        user_d1.email = "diana.prince@justice.org"  # This works
        print(f"Updated: {user_d1}")

        print("\nAttempting invalid email assignments:")
        # This will raise an error
        user_d2 = UserDescriptor("eve", "bad-email")
        print(f"Created: {user_d2}")  # This won't be reached
    except (TypeError, ValueError) as e:
        print(f"Error caught: {e}")

    print("\n--- Another attempt with invalid email (empty string) ---")
    try:
        user_d3 = UserDescriptor("frank", "")
    except (TypeError, ValueError) as e:
        print(f"Error caught: {e}")

    print("\n--- Another attempt with invalid email (not a string) ---")
    try:
        user_d4 = UserDescriptor("grace", 12345)
    except (TypeError, ValueError) as e:
        print(f"Error caught: {e}")

    print("\n--- Company Test! ---")

    try:
        company1 = Company("Acme Inc.", "admin@acme.com", "info@acme.com")
        print(f"Created: {company1}")
        company1.admin_email = "new.admin@acme.co"
        print(f"Updated: {company1}")

        company2 = Company("Widgets LLC", "bad-admin", "good@widgets.com")
    except (TypeError, ValueError) as e:
        print(f"Error caught for Company: {e}")

