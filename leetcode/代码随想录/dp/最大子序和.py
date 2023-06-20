class Solution:
    def maxSubArray(self, nums):
        n = len(nums)
        dp = [0]*n
        dp[0] = nums[0]
        for i in range(1,n):
            dp[i] = max(dp[i-1]+nums[i],nums[i])
        res = max(dp)
        return res

nums = [-2,1,-3,4,-1,2,1,-5,4]
test = Solution()
print(test.maxSubArray(nums))