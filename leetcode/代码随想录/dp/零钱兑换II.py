class Solution:
    # 如果求组合数就是外层for循环遍历物品，内层for遍历背包。
    #
    # 如果求排列数就是外层for遍历背包，内层for循环遍历物品。
    def change(self, amount, coins):
        n = len(coins)
        dp = [[0]*(amount+1) for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0] = 1
        for i in range(1,n+1):
            for j in range(1,amount+1):
                if coins[i-1] > j:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-coins[i-1]]
        return dp[-1][-1]

test = Solution()
amount = 5
coins = [1, 2, 5]
print(test.change(amount,coins))
