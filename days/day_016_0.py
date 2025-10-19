def max_turbulent_size(lst):
    # Algorithm using two pointer approach
    l_idx, r_idx, max_len, prev = 0, 1, 1, ""

    while r_idx < len(lst):
        if lst[r_idx - 1] > lst[r_idx] and prev != ">":
            max_len = max(max_len, r_idx - l_idx + 1)
            r_idx = r_idx + 1
            prev = ">"
        elif lst[r_idx - 1] < lst[r_idx] and prev != "<":
            max_len = max(max_len, r_idx - l_idx + 1)
            r_idx = r_idx + 1
            prev = "<"
        else:
            if lst[arr_idx] == lst[arr_idx - 1]:
                arr_idx = arr_idx + 1
            l_idx = r_idx - 1  # Jump to the point where it makes sense to start
            prev = ""

    return max_len
