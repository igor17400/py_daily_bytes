def product_except_self(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    len_ = len(nums)
    output = [1] * len_

    prefix = 1
    for i in range(len_):
        output[i] = prefix
        prefix *= nums[i]

    print("output only with prefix: ", output)

    postfix = 1
    for j in range(len_ - 1, -1, -1):  # reverse for loop
        output[j] *= postfix
        postfix *= nums[j]

    return output

nums = [1,2,3,4]
print(product_except_self(nums))
print("----")
nums = [-1,1,0,-3,3]
print(product_except_self(nums))
