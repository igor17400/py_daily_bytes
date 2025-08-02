###############
# Day 6: Creating Data Classes with @dataclass
###############

"""
Goal:
Demonstrate how to create a clean, readable, and full-featured data class with minimal 
boilerplate code using the @dataclass decorator.
"""

###############
# The Traditional Boilerplate Approach
###############

class UserTraditional:
    """ A user class with manually-written __init__, __repr__, and __eq__. """
    def __init__(self, user_id: int, username: str, is_active: bool = True):
        self.user_id = user_id
        self.username = username
        self.is_active = is_active

    def __repr__(self):
        return (
            f"UserTraditional(user_id={self.user_id!r}, "
            f"username={self.username!r}, is_active={self.is_active!r})"
        )

    def __eq__(self, other):
        if not isinstance(other, UserTraditional):
            return NotImplemented
        return (
                self.user_id == other.user_id and
                self.username == other.username and
                self.is_active == other.is_active
        )

if __name__ == "__main__":
    print("--- Traditional Class Example ---")
    user1 = UserTraditional(1, "alice")
    user2 = UserTraditional(2, "bob")
    user3 = UserTraditional(1, "alice")

    print(f"User 1: {user1}")
    print(f"User 2: {user2}")

    print(f"user1 == user2? {user1 == user2}")
    print(f"user1 == user3? {user1 == user3}")
