def sliding_window(lst):
    len_ = len(lst)
    max_sum = lst[0]
    curr_sum = 0
    max_l, max_r = 0, 0
    l_idx = 0

    if len_ == 1:
        return max_sum

    for r_idx in range(1, len_):
        if curr_sum < 0:
            curr_sum = 0
            l_idx = r_idx

        curr_sum += lst[r_idx]
        if curr_sum > max_sum:
            max_sum = curr_sum
            max_l, max_r = l_idx, r_idx

    subarray = lst[max_l:max_r + 1]
    return sum(subarray), subarray


lst = [5, 4, -1, 7, 8]
print("List: ", lst)
sum_, subarray = sliding_window(lst)
print("Sum: ", sum_)
print("Subarray: ", subarray)

print("--------")

lst = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print("List: ", lst)
sum_, subarray = sliding_window(lst)
print("Sum: ", sum_)
print("Subarray: ", subarray)
