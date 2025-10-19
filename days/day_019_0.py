def max_area(height):
    """
    :type height: List[int]
    :rtype: int
    """
    l_idx, r_idx = 0, len(height) - 1
    max_area = 0

    while l_idx < r_idx:
        ret_base = r_idx - l_idx
        min_height = min(height[l_idx], height[r_idx])
        area = ret_base * min_height
        max_area = max(max_area, area)

        if height[l_idx] < height[r_idx]:
            l_idx += 1
        else:
            r_idx -= 1

    return max_area

height = [1,8,6,2,5,4,8,3,7]
print(max_area(height))
print("-----")
height = [1,1]
print(max_area(height))
