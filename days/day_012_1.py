###############
# Day 12: Collections with defaultdict and Counter
###############

from collections import defaultdict, Counter

# The goal is to analyze this list of fruits.
fruits = [
    "apple", "banana", "cherry", "apple", "date", "banana",
    "elderberry", "fig", "apple", "grape", "cherry"
]

# --- The Modern Approach (using defaultdict and Counter) ---
print("--- Modern Approach: defaultdict and Counter ---")

# Counter is designed for this exact problem!
# It automatically handles the counting.
fruit_counts_counter = Counter(fruits)
print(f"Counter fruit counts: {fruit_counts_counter}")

# defaultdict is perfect for grouping, as it automatically
# provides a default value (in this case, an empty list)
# for any new key you access.
fruits_by_letter_defaultdict = defaultdict(list)
for fruit in fruits:
    first_letter = fruit[0]
    fruits_by_letter_defaultdict[first_letter].append(fruit)

print(f"defaultdict grouping by first letter: {fruits_by_letter_defaultdict}")
