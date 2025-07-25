###############
# Day 0: One-Liner List Compressor
###############
data = [1, 2, 3, 3, 4, 4, 5, 5, 6, 6]
unique_data = list(dict.fromkeys(data))

print(f"Original: {data}")
print(f"Unique: {unique_data}")
