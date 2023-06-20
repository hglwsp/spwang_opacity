def minimumTotal(triangle):
    n = len(triangle)
    dp = [[0]*n for _ in range(n)]
    dp[0][0] = triangle[0][0]
    for i in range(1,n):
        dp[i][0] = dp[i-1][0]+triangle[i][0]
        dp[i][i] = dp[i-1][i-1] + triangle[i][i]
    for a in range(1,n):
        for b in range(1,a):
            dp[a][b] = min(dp[a-1][b],dp[a-1][b-1]) + triangle[a][b]
    return min(dp[n - 1])