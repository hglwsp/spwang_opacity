class Solution:
    def canPartition(self, nums):
        sumall,n = sum(nums),len(nums)
        if sumall % 2!=0:
            return False
        target = sumall // 2
        dp = [[False]*(target+1) for _ in range(n+1)]
        dp[0][0] = True
        for a in range(1,n+1):
            for b in range(0,target+1):
                if b < nums[a-1]:
                    dp[a][b] = dp[a-1][b]
                else:
                    dp[a][b] = dp[a-1][b] | dp[a-1][b-nums[a-1]]
        return dp[n][target]

nums = [1,5,11,5]
test = Solution()
print(test.canPartition(nums))