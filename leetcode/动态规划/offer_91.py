def minCost(costs):
    n = len(costs)
    # dp row:n  col:3
    dp = [[0] * 3 for _ in range(n)]
    # bound
    for i in range(3):
        dp[0][i] = costs[0][i]
    for row in range(1,n):
        dp[row][0] = min(dp[row - 1][1], dp[row - 1][2]) + costs[row][0]
        dp[row][1] = min(dp[row - 1][0], dp[row - 1][2]) + costs[row][1]
        dp[row][2] = min(dp[row - 1][0], dp[row - 1][1]) + costs[row][2]
    return min(dp[-1])

costs = [[17,2,17],[16,16,5],[14,3,19]]
print(minCost(costs))