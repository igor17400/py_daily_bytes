def brute_force(lst: list) -> int:
    """
    :type lst: List[int]
    :rtype: int
    """
    len_ = len(lst)
    max_sum = lst[0]
    idx_r, idx_l = 0, 0

    if len_ == 1:
        return lst[0]

    for i in range(0, len_):
        curr_sum = 0
        for j in range(i, len_):
            curr_sum += lst[j]
            max_sum_tmp = max(curr_sum, max_sum)
            if max_sum_tmp > max_sum:
                max_sum = max_sum_tmp
                idx_l = i
                idx_r = j

    print("Maximum Subarray: ", lst[idx_l:idx_r + 1])
    print("Largest sum: ", max_sum)

    return max_sum


lst = [5, 4, -1, 7, 8]
print("List: ", lst)
brute_force(lst)

print("--------")

lst = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print("List: ", lst)
brute_force(lst)
