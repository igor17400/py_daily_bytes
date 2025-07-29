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


############
# The walrus operator allow us to assign the result of an
# expression to a variable as part of a larger expression.
# Thereby, combining assignment and usage in a single step.
############

def process_numbers_walrus():
    print("--- Processing Numbers (With Walrus Operator) ---")
    print("Enter positive numbers. Press Enter on an empty line to quit, or type non-numeric to quit.")

    while (user_input := input("Enter a number: ")) and user_input.strip():
        try:
            if (num := int(user_input)) > 0:
                sqrt_num = math.sqrt(num)
                print(f"  The square root of {num} is {sqrt_num:.2f}")
            else:
                print(f"  {num} is not a positive number. Skipping square root.")

        except ValueError:
            # Handle non-numeric input
            print(f"Invalid input '{user_input}'. Not a valid number. Exiting.")
            break  # Exit the loop if input is not a valid number
    else:
        print("Empty result detected. Existing.")


if __name__ == "__main__":
    process_numbers_walrus()
