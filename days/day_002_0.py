###############
# Day 2:  The Walrus Operator (:=)
###############

"""
Goal:

Process a stream of numerical user inputs. For each input,
convert it to an integer. If the integer is positive,
calculate its square root and print it. Continue processing
inputs until the user enters an empty line (just presses
Enter) or enters a non-numeric value.
"""

import math


def process_numbers_traditional():
    print("--- Processing Numbers (Traditional Approach) ---")
    print("Enter positive numbers. Press Enter on an empty line to quit, or type non-numeric to quit.")

    while True:
        user_input = input("Enter a number:")

        # Check for empty input to quit
        if not user_input:
            print("Empty result detected. Existing.")
            break

        try:
            num = int(user_input)
            if num > 0:
                sqrt_num = math.sqrt(num)
                print(f"  The square root of {num} is {sqrt_num:.2f}")
            else:
                print(f"  {num} is not a positive number. Skipping square root.")
        except ValueError:
            # Handle non-numeric input
            print(f"Invalid input '{user_input}'. Not a valid number. Exiting.")
            break


if __name__ == "__main__":
    process_numbers_traditional()
