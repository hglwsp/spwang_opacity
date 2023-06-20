def search(nums, target):
    n = len(nums)
    if n == 0:
        return -1

    left = 0
    right = n - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] > target:
            right = mid - 1
        if nums[mid] < target:
            left = mid + 1
    return -1