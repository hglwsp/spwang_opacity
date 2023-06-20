class Solution:
    def integerBreak(self, n):
        # dp[i], 分解i得到最大的
        dp = [0]*(n+1)
        dp[2] = 1
        for i in range(3,n+1):
            for j in range(0,i-1):
                dp[i] = max(dp[i],(i-j)*j,dp[j]*(i-j))
        return dp[n]

n = 10
test = Solution()
print(test.integerBreak(n))