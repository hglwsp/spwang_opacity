class Solution:
    def uniquePaths(self, m, n):
        dp = [[0]*n for _ in range(m)]
        dp[0][0] = 1
        for i in range(1,m):
            dp[i][0] = dp[i-1][0] = 1
        for j in range(1,n):
            dp[0][j] = dp[0][j-1] = 1
        for a in range(1,m):
            for b in range(1,n):
                dp[a][b] = dp[a-1][b] + dp[a][b-1]
        return dp[-1][-1]

test = Solution()
m = 1
n = 1
print(test.uniquePaths(m,n))