def maxValue(grid):
    # row,column
    m = len(grid)
    n = len(grid[0])
    dp = [[0]*n for _ in range(m)]
    # bound
    dp[0][0] = grid[0][0]
    for i in range(1,m):
        dp[i][0] = dp[i-1][0] + grid[i][0]
    for j in range(1,n):
        dp[0][j] = dp[0][j-1] + grid[0][j]
    for row in range(1,m):
        for col in range(1,n):
            dp[row][col] = max(dp[row-1][col],dp[row][col-1]) + grid[row][col]
    return dp[-1][-1]

grid = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]

print(maxValue(grid))