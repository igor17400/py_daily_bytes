def can_partition(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    total_sum = sum(nums)
    if total_sum % 2 != 0:
        return False

    # dp array
    len_ = len(nums)
    target_sum = total_sum // 2
    dp = [[False] * (target_sum + 1) for _ in range(len_ + 1)]

    # Base case 1
    for i in range(len_ + 1):
        dp[i][0] = True

    # Whole matrix
    for i in range(1, len_ + 1):
        current_num = nums[i - 1]
        for j in range(1, target_sum + 1):
            # Option 1 - exclude the item
            exclude = dp[i - 1][j]

            # Option 2 - include the item
            include = False
            if j >= current_num:
                include = dp[i - 1][j - current_num]

            dp[i][j] = exclude or include

    return dp[len_][target_sum]

nums = [1, 5, 11, 5]
print(can_partition(nums))