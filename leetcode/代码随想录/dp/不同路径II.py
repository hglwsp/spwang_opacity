class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0]*n for _ in range(m)]
        if obstacleGrid[0][0] == 1:
            return 0
        else:
            dp[0][0] = 1
        for i in range(1,m):
            if obstacleGrid[i][0] == 1:
                continue
            else:
                dp[i][0] = dp[i-1][0]
        for j in range(1,n):
            if obstacleGrid[0][j] == 1:
                continue
            else:
                dp[0][j] = dp[0][j-1]
        for a in range(1,m):
            for b in range(1,n):
                if obstacleGrid[a][b] == 1:
                    continue
                else:
                    dp[a][b] = dp[a-1][b] + dp[a][b-1]
        return dp[-1][-1]

test = Solution()
obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
print(test.uniquePathsWithObstacles(obstacleGrid))