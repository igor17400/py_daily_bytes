###############
# Day 5: Memory Efficiency with __slots__
###############

"""
Goal:

Reduce memory footprint of objects in a class by using __slots__ and
demonstrate the memory savings with a simple example.
"""

###############
# Approach without __slots__
###############

import sys

class PointWithDict:
    """
    A simple 2D point class with standard __dict__ for attributes.
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return f"PointWithDict(x={self.x}, y={self.y})"

def show_memory_usage(obj):
    """
    Measures and prints the memory usage for a class object or an instance.
    This function will automatically detect what kind of object it is.
    """
    obj_type_name = "Class" if isinstance(obj, type) else "Instance"
    obj_class_name = obj.__name__ if isinstance(obj, type) else obj.__class__.__name__
    obj_size = sys.getsizeof(obj)

    # Let's also check for the size of the instance's __dict__
    dict_size = sys.getsizeof(obj.__dict__)
    print(f"[{obj_class_name} as {obj_type_name}]")
    print(f"  - Object size (including __dict__ overhead): {obj_size} bytes")
    print(f"  - Size of __dict__: {dict_size} bytes")
    print(f"  - Total: {obj_size + dict_size} bytes\n")

if __name__ == "__main__":
    print("--- Comparing Class vs. Instance Memory ---")
    # 1. Measure the class object itself
    show_memory_usage(PointWithDict)

    # 2. Measure an instance of the class
    p_dict = PointWithDict(10, 20)
    show_memory_usage(p_dict)

    # Let's verify the memory doesn't change on a single attribute addition
    print("--- Adding a new attribute to the instance ---")
    p_dict.z = 30
    print(f"Added new attribute 'z' with value: {p_dict.z}")
    show_memory_usage(p_dict)
