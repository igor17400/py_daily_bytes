###############
# Day 5: Memory Efficiency with __slots__
###############

"""
Goal:

Reduce memory footprint of objects in a class by using __slots__ and
demonstrate the memory savings with a simple example.
"""

###############
# Approach using the __slot__
###############

import sys

class PointWithSlots:
    """
    A 2D point class that uses __slots__ to save memory.
    It does not have a __dict__ and only allows attributes listed in __slots__
    """
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return f'PointWithSlots({self.x}, {self.y})'

def show_memory_usage(obj):
    """
    Measures and prints the memory usage for a class object or an instance.
    This function will automatically detect what kind of object it is.
    """
    obj_type_name = "Class" if isinstance(obj, type) else "Instance"
    obj_class_name = obj.__name__ if isinstance(obj, type) else obj.__class__.__name__
    obj_size = sys.getsizeof(obj)

    try:
        dict_size = sys.getsizeof(obj.__dict__)
        print(f"[{obj_class_name} as {obj_type_name}]")
        print(f"  - Object size (including __dict__ overhead): {obj_size} bytes")
        print(f"  - Size of __dict__: {dict_size} bytes")
        print(f"  - Total: {obj_size + dict_size} bytes\n")
    except AttributeError: # error will be thrown when adding a parameter
        print(f"[{obj_class_name} as {obj_type_name}]")
        print(f"  - Object size: {obj_size} bytes")
        print(f"  - No __dict__ attribute found.")


if __name__ == "__main__":
    print("\n--- Examining PointWithSlots Class and Instances ---")

    # 1. Measure the class object itself
    show_memory_usage(PointWithSlots)

    # 2. Measure an instance of the class
    p_slots = PointWithSlots(10, 20)
    show_memory_usage(p_slots)

    print("\n--- Trying to add new attribute to PointWithSlots ---")
    try:
        p_slots.z = 30  # This will raise an error!
    except AttributeError as e:
        print(f"Caught expected error: {e}")

