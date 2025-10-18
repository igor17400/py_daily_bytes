def kadanes_algorithm(lst):
    """
    :type lst: List[int]
    :rtype: int
    """
    len_ = len(lst)
    max_sum = lst[0]
    curr_sum = 0

    if len_ == 1:
        return max_sum

    for i in range(len_):
        curr_sum = max(curr_sum, 0)
        curr_sum += lst[i]
        max_sum = max(curr_sum, max_sum)


    print("Largest sum: ", max_sum)

    return max_sum

lst = [5, 4, -1, 7, 8]
print("List: ", lst)
kadanes_algorithm(lst)

print("--------")

lst = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print("List: ", lst)
kadanes_algorithm(lst)

