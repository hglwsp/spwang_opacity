def maxRotateFunction(nums):
    n = len(nums)
    tol = sum(nums)
    dp = [0]*n
    for i in range(0,n):
        dp[0] += i*nums[i]
    for j in range(1,n):
        dp[j] = dp[j-1] + tol - n*nums[-j]
    return max(dp)

nums = [4,3,2,6]
print(maxRotateFunction(nums))
