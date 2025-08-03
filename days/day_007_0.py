###############
# Day 7: Lambda Functions
###############

"""
Goal:
Demonstrate the syntax and a common use case of lambda functions, and highlight
their primary limitation by comparing them to a traditional def function.
"""

###############
# The Traditional Approach For Creating Functions
###############

def is_even(num):
    """Checks if a number is even."""
    return num % 2 == 0

def square(num):
    """Returns the square of a number."""
    return num ** 2

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6]
    print("--- Using traditional def functions with map and filter ---")

    # Use a def function with `filter`
    evens = list(filter(is_even, numbers))
    print(f"Original numbers: {numbers}")
    print(f"Even numbers: {evens}")

    # Use a def function with `map`
    squares = list(map(square, numbers))
    print(f"Squares of numbers: {squares}")
