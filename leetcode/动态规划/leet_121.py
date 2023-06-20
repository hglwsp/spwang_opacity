# 买卖股票最佳时机
# 你只能选择某一天买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。计算你所能获取的最大利润。
# input:[7,1,5,3,6,4]
# output:5
# dp[] = {0,0,4,4,5,5} =
# dp[i]= max{dp[i-1],price[i] - min}
def maxProfit(prices):
    l = len(prices)
    dp = {}
    dp[0] = 0
    min_price = prices[0]
    for i in range(1,l):
        dp[i] = max(dp[i-1],prices[i] - min_price)
        min_price = min(prices[i],min_price)
    return dp[l - 1]

prices = [7,1,5,3,6,4]
print(maxProfit(prices))