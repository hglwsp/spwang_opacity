def numWays(n):
    if n < 2: return 1
    dp = [0]*(n+1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2,n+1):
        dp[i] = dp[i-2] + dp[i-1]
    return dp[n] % 1000000007

n = 7
print(numWays(n))