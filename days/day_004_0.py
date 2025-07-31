###############
# Day 4: Memoization
###############

"""
Goal:

Memoization is an optimization technique where you store the results
of expensive function calls and return the cached result when the same
inputs occur again.
"""

###############
# Slow Approach
###############

import time


def fibonacci_slow(n):
    """
    Calculates the n-th Fibonacci number using naive recursion.
    This is very inefficient for larger 'n' due to repeated calculations.
    """
    if n <= 1:
        return n
    return fibonacci_slow(n - 1) + fibonacci_slow(n - 2)


if __name__ == '__main__':
    print("--- Naive Recursive Fibonacci (SLOW) ---")

    print("Calculating fibonacci_slow(30)... (might take a moment)")
    start_time = time.perf_counter()
    result_slow = fibonacci_slow(30)  # Try 35 or 40 for a dramatic difference!
    end_time = time.perf_counter()
    print(f"fibonacci_slow(30) = {result_slow}")
    print(f"Time taken: {end_time - start_time:.4f} seconds.")
