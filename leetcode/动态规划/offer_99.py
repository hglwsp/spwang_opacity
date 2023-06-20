def minPathSum(grid):
    # row:m,column:n
    m = len(grid)
    n = len(grid[0])
    dp = [[0]*n for _ in range(m)]
    # only under and right
    dp[0][0] = grid[0][0]
    # fill bound
    tmprow = tmpcol = grid[0][0]
    for i in range(1,m):
        tmprow +=grid[i][0]
        dp[i][0] = tmprow
    for j in range(1,n):
        tmpcol += grid[0][j]
        dp[0][j] = tmpcol
    # state translate
    for a in range(1,m):
        for b in range(1,n):
            dp[a][b] = min(dp[a-1][b],dp[a][b-1]) + grid[a][b]
    return dp[m-1][n-1]

grid = [[1,3,1],[1,5,1],[4,2,1]]
print(minPathSum(grid))