def minPathSum(grid):
    if not grid or not grid[0]:
        return 0
    rows,columns = len(grid),len(grid[0])
    dp = [[0] * columns for _ in range(rows)]
    dp[0][0] = grid[0][0]
    # i > 0, dp[i][0] = dp[i-1][0] + grid[i][0]
    # j > 0, dp[0][j] = dp[0][j-1] + grid[0][j]
    #dp[i][j] = min(dp[i-1][j],dp[i,j-1])+grid[i][j]
    for i in range(1,rows):
        dp[i][0] = dp[i-1][0] + grid[i][0]
    for j in range(1,columns):
        dp[0][j] = dp[0][j-1] + grid[0][j]
    for a in range(1,rows):
        for b in range(1,columns):
            dp[a][b] = min(dp[a-1][b], dp[a][b-1]) + grid[a][b]
    return dp[rows-1][columns-1]

grid = [[1,3,1],[1,5,1],[4,2,1]]
print(minPathSum(grid))
