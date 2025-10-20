def dfs_helper(i, strs, cap_m, cap_n, memo):
    if i == len(strs):
        return 0

    current_state_key = (i, cap_m, cap_n)
    if current_state_key in memo:
        return memo[current_state_key]

    # Skip item i
    lg_subset = dfs_helper(i + 1, strs, cap_m, cap_n, memo)

    # Include item i
    new_cap_m = cap_m - strs[i].count("0")
    new_cap_n = cap_n - strs[i].count("1")
    if new_cap_m >= 0 and new_cap_n >= 0:
        len_subset = 1 + dfs_helper(i + 1, strs, new_cap_m, new_cap_n, memo)
        lg_subset = max(lg_subset, len_subset)

    # Cache the result for the current state (i, cap_m, cap_n)
    memo[current_state_key] = lg_subset

    return lg_subset


def dfs(strs, cap_m, cap_n):
    memo = {}
    return dfs_helper(0, strs, cap_m, cap_n, memo)


def find_max_form(strs, m, n):
    """
    :type strs: List[str]
    :type m: int
    :type n: int
    :rtype: int
    """
    return dfs(strs, m, n)

strs = ["10","0001","111001","1","0"]
print(find_max_form(strs, 5, 3))
