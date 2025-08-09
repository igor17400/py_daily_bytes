###############
# Day 12: Collections with defaultdict and Counter
###############

fruits = [
    "apple", "banana", "cherry", "apple", "date", "banana",
    "elderberry", "fig", "apple", "grape", "cherry"
]

# --- The Traditional Approach (without specialized collections) ---
print("--- Traditional Approach: Manual Counting and Grouping ---")
fruit_counts_manual = {}
for fruit in fruits:
    # This check is boilerplate and adds verbosity.
    if fruit in fruit_counts_manual:
        fruit_counts_manual[fruit] += 1
    else:
        fruit_counts_manual[fruit] = 1

print(f"Manual fruit counts: {fruit_counts_manual}")

# To group fruits by their first letter, we need a similar check.
fruits_by_letter_manual = {}
for fruit in fruits:
    first_letter = fruit[0]
    if first_letter in fruits_by_letter_manual:
        fruits_by_letter_manual[first_letter].append(fruit)
    else:
        fruits_by_letter_manual[first_letter] = [fruit]

print(f"Manual grouping by first letter: {fruits_by_letter_manual}\n")
