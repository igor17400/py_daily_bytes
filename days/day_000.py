###############
# Day 0: One-Liner List Compressor
###############
data = [1, 2, 3, 3, 4, 4, 5, 5, 6, 6]
unique_data = list(dict.fromkeys(data))

print(f"Original: {data}")
print(f"Unique: {unique_data}")

##############
# Code Explanation
##############
"""
1.  data initializes a list containing several integer values, including some duplicates (e.g., 3, 4, 5, 6 appear twice).

2.  unique_data = list(dict.fromkeys(data)) This is the core of the "one-liner" compression. Let's breakdown:

    - dict.fromkeys(data): This is a class method of dictionaries. When given an iterable (like our `data` list), 
    it creates a new dictionary where each unique element from the iterable becomes a key, and their values are set to `None` by default. 
    The crucial point here is that dictionary keys *must be unique*. So, when dict.fromkeys() processes [1, 2, 3, 3, ...], it only keeps 
    the first occurrence of each number as a key.
    
    - list(...): This converts the keys of the dictionary back into a list. 
"""