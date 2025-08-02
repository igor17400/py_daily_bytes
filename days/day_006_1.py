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

from dataclasses import dataclass, field

@dataclass(frozen=True)  # Makes the object immutable
class User:
    """
    A user class created with @dataclass. All methods are auto-generated.
    """
    user_id: int
    username: str
    # Use field() for mutable defaults or metadata
    is_active: bool = field(default=True)


if __name__ == "__main__":
    print("\n--- @dataclass Example ---")
    user1 = User(1, "alice")
    user2 = User(2, "bob", is_active=False)
    user3 = User(1, "alice")

    print(f"User 1: {user1}")
    print(f"User 2: {user2}")

    print(f"user1 == user2? {user1 == user2}")
    print(f"user1 == user3? {user1 == user3}")

    print("\n--- The dataclass is frozen and immutable ---")
    try:
        user1.username = "new_alice"  # This will raise an error!
    except AttributeError as e:
        print(f"Caught expected error: {e}")
