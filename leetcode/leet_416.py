def canPartition(nums):
    sumall,n = sum(nums),len(nums)
    if sumall % 2!=0:
        return False
    target = sumall // 2
    # 初始化
    dp = [[False] * (target + 1) for _ in range(n + 1)]
    # dp[i][j]: 从前i个元素中选出若干个数字刚好能够组成j
    dp[0][0] = True
    for i in range(1,n+1):
        for j in range(target+1):
            if j < nums[i - 1]:  # 容量有限，无法选择第i个数字nums[i-1]
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
    return dp[n][target]



