###############
# Day 1: Function Timer Decorator
###############

import time


def time_decorator(func):
    """
    A Decorator that prints the time a function takes to execute.
    """

    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f"{func.__name__} took {total_time} seconds.")
        return result

    return wrapper


@time_decorator
def slow_function(delay_time):
    """A sample function that just waits for a bit"""
    print(f"Sleeping for {delay_time} seconds...")
    time.sleep(delay_time)
    print("Execution finished.")
    return "Done!"

if __name__ == "__main__":
    slow_function(10)


