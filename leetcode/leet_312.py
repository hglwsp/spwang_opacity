def maxCoins(nums):
    n = len(nums)
    nums = [1] + nums + [1]
    dp = [[0] * (n+2) for _ in range(n+2)]
    # dp[0][n+1]
    for i in range(n,-1,-1):
        for j in range(i+1,n+2):
            for k in range(i+1,j):
                dp[i][j] = max(dp[i][j],nums[i]*nums[k]*nums[j] + dp[i][k]+dp[k][j])
    return dp[0][n+1]

nums = [3,1,5,8]
print(maxCoins(nums))