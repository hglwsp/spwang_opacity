class Solution:
    def climbStairs(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        dp = [0] * (n+1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3,n+1):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[n]

test = Solution()
n = 4
print(test.climbStairs(n))