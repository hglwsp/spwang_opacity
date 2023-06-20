def numSubarrayProductLessThanK(nums, k):
    cur = 1
    left = 0
    ans = 0
    for right,num in enumerate(nums):
        cur*=num
        while left <= right and cur >= k:
            cur //= nums[left]
            left+=1
        ans += right - left + 1
    return ans

nums = [10,5,2,6]
k = 100
print(numSubarrayProductLessThanK(nums,k))