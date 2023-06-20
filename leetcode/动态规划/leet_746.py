# 使用最小花费爬楼梯
# 每当你爬上一个阶梯你都要花费对应的体力值，一旦支付了相应的体力值，你就可以选择向上爬一个阶梯或者爬两个阶梯。
# 请你找出达到楼层顶部的最低花费。在开始时，你可以选择从下标为 0 或 1 的元素作为初始阶梯。
# 输入：cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
# 输出：6
# dp[i] = min(dp[i -1] + cost[i-1],dp[i-2]+cost[i-2])
def minCostClimbingStairs(cost):
    l = len(cost)
    dp = [0] * (l + 1)
    for i in range(2,l+1):
        dp[i] = min(dp[i-1]+ cost[i-1] ,dp[i-2] + cost[i-2])
    return dp[-1]

cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
print(minCostClimbingStairs(cost))