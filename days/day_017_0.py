def num_of_subarrays(arr, k, threshold):
    """
    :type arr: List[int]
    :type k: int
    :type threshold: int
    :rtype: int
    """
    subarray_window = []
    l_idx = 0
    len_ = len(arr)
    counter = 0

    for r_idx in range(len_):
        if r_idx - l_idx + 1 > k: # Size of our window
            subarray_window.remove(subarray_window[0])
            l_idx += 1
        subarray_window.append(arr[r_idx])

        if len(subarray_window) == k:
            avg = sum(subarray_window)/len(subarray_window)
            if avg >= threshold:
                counter += 1

    return counter


arr = [2,2,2,2,5,5,5,8]
k = 3
threshold = 4
print("Array: ", arr)
print("k: ", k)
print("Threshold: ", threshold)
print("Output: ", num_of_subarrays(arr, k, threshold))

print("----------")

arr = [11,13,17,23,29,31,7,5,2,3]
k = 3
threshold = 5
print("Array: ", arr)
print("k: ", k)
print("Threshold: ", threshold)
print("Output: ", num_of_subarrays(arr, k, threshold))
