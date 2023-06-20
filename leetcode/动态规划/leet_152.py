# 输入: nums = [2,3,-2,4]
# 输出: 6
def maxProduct(nums):
    l = len(nums)
    if l < 2:
        return nums[0]
    dp_max = [0] * l
    dp_max[0] = nums[0]
    dp_min = [0] * l
    dp_min[0] = nums[0]
    res = nums[0]

    for i in range(1,l):
        dp_max[i] = max(dp_max[i-1]*nums[i], nums[i], dp_min[i-1]*nums[i])
        dp_min[i] = min(dp_max[i-1] * nums[i], nums[i], dp_min[i-1] * nums[i])
        res = max(res, dp_max[i])
    return res

nums = [2,-1,1,1]
print(maxProduct(nums))