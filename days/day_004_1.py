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
# Memoization with lru_cache
###############

import time
import functools


# maxsize = None --> means the cache can grow indefinitely
@functools.lru_cache(maxsize=None)
def fibonacci_fast(n):
    """
    Calculates the n-th Fibonacci number using recursion with
    memoization.

    The @functools.lru_cache decorator caches results to
    prevent re-calculation.
    """
    if n <= 1:
        return n
    return fibonacci_fast(n - 1) + fibonacci_fast(n - 2)


if __name__ == "__main__":
    print("\n--- Optimized Recursive Fibonacci (FAST) with @lru_cache ---")

    print("Calculating fibonacci_fast(30)...")
    start_time = time.perf_counter()
    result_fast = fibonacci_fast(30)
    end_time = time.perf_counter()
    print(f"fibonacci_fast(30) = {result_fast}")
    print(f"Time taken: {end_time - start_time:.8f} seconds")
