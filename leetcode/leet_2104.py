# 给你一个整数数组 nums 。nums 中，子数组的 范围 是子数组中最大元素和最小元素的差值。
# 返回 nums 中 所有 子数组范围的 和 。
# 子数组是数组中一个连续 非空 的元素序列。


# 输入：nums = [1,2,3]
# 输出：4

def subArrayRanges(nums):
    ans, n = 0, len(nums)
    for i in range(n):
        minVal, maxVal = 1e9,-1e9
        for j in range(i, n):
            minVal = min(minVal, nums[j])
            maxVal = max(maxVal, nums[j])
            ans += maxVal - minVal
    return ans


nums = [4,-2,-3,4,1]
print(subArrayRanges(nums))