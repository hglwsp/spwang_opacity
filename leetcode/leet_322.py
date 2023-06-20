def coinChange(coins, amount):
    dp = [0] + [10001] * amount
    for coin in coins:
        for i in range(coin,amount+1):
            dp[i] = min(dp[i],dp[i-coin]+1)      #是否挑选这个硬币
    return dp

test = [1, 2, 5]
amount = 11
print(coinChange(test,amount))
