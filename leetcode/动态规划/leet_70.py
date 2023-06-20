# 爬楼梯
# 每次你可以爬 1 或 2 个台阶，多少种不同的方法可以爬到楼顶
# input:2   output:2   a:1+1,b:2
# dp[n] = dp[n-1] + dp[n-2]
def climbStairs(n):
    dp = {}
    dp[0] = 0
    dp[1] = 1
    dp[2] = 2
    for i in range(3,n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

test = 3
print(climbStairs(test))