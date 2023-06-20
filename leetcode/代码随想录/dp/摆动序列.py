class Solution:
    def wiggleMaxLength(self, nums):
        n = len(nums)
        dp = [[1]*2 for _ in range(n)]
        for i in range(1,n):
            for j in range(0,i):
                if nums[j] > nums[i]:
                    # i 做山谷
                    dp[i][1] = max(dp[i][1],dp[j][0]+1)
                if nums[j] < nums[i]:
                    # i做山峰
                    dp[i][0] = max(dp[i][0],dp[j][1]+1)
        return max(dp[n-1])

test = Solution()
nums = [1,7,4,9,2,5]
print(test.wiggleMaxLength(nums))