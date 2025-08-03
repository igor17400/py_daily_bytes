###############
# Day 7: Lambda Functions
###############

"""
Goal:
Demonstrate the syntax and a common use case of lambda functions, and highlight
their primary limitation by comparing them to a traditional def function.
"""

###############
# Creating functions using lambda
###############

if __name__ == '__main__':
    # Instead of creating the definitions as done above we can...
    numbers = [1, 2, 3, 4, 5, 6]
    print("--- Using lambda functions with map and filter ---")

    # Use filter with lambda function
    evens = list(filter(lambda x: x % 2 == 0, numbers))
    print(f"Original numbers: {numbers}")
    print(f"Even numbers: {evens}")

    # Use map with lambda function
    squares = list(map(lambda x: x ** 2, numbers))
    print(f"Square numbers: {squares}")
