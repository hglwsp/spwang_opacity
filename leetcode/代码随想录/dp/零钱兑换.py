class Solution:
    def coinChange(self, coins, amount):
        # dfs 超时
        # res = []
        # path = []
        # coins.sort()
        # self.sumnow = 0
        # def backtrack(nums,startindex):
        #     if self.sumnow == amount:
        #         res.append(path[:])
        #         return
        #     if self.sumnow > amount:
        #         return
        #     for i in range(startindex,len(nums)):
        #         self.sumnow += nums[i]
        #         path.append(nums[i])
        #         backtrack(nums,0)
        #         path.pop()
        #         self.sumnow -= nums[i]
        # backtrack(coins,0)
        # tmp = 999
        # for i in range(len(res)):
        #     tmp = min(tmp,len(res[i]))
        # if tmp == 999:
        #     return -1
        # else:return tmp

        # dp
        dp = [amount+1]*(amount+1)
        dp[0] = 0
        for j in range(1,amount+1):
            for coin in coins:
                if j >= coin:
                    dp[j] = min(dp[j-coin]+1,dp[j])
        return dp[amount] if dp[amount] < amount + 1 else -1

coins = [1, 2, 5]
amount = 11
test = Solution()
print(test.coinChange(coins,amount))