def twoEggDrop(n):
    dp = [[float('inf')] * 2 for _ in range(n + 1)]
    dp[0]= [0,0]
    for i in range(1,n+1):
        # 只有一个蛋蛋，从下往上
        dp[i][0] = i
        # 两个蛋蛋
        for k in range(1,i+1):
            dp[i][1] = min(dp[i][1],max(dp[k-1][0],dp[i-k][1])+1)
    return dp[n][1]