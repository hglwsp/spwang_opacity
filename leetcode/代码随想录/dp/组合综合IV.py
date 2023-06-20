class Solution:
    # 完全背包先遍历背包，再遍历物品
    def combinationSum4(self, nums, target):
        # dp
        # n = len(nums)
        # nums.sort()
        # dp = [[0]*(n+1) for _ in range(target+1)]
        # dp[0][0] = 1
        # for i in range(1,n+1):
        #     dp[0][i] = 1
        # for i in range(1,target+1):
        #     for j in range(1,n+1):
        #         if i < nums[j-1]:
        #             dp[i][j] = dp[i][j-1]
        #         else:
        #             # 重复，先找前面的
        #             for k in range(0,j):
        #                 dp[i][j] += dp[i-nums[k]][j]
        # return dp[target][n]

        # dfs 如果本题要把排列都列出来的话，只能使用回溯算法爆搜。
        # res = []
        # path = []
        # nums.sort()
        # self.sumnow = 0
        # def backtrack(nums,startindex):
        #     if self.sumnow == target:
        #         res.append(path[:])
        #         return
        #     if self.sumnow > target:
        #         return
        #     for i in range(startindex,len(nums)):
        #         self.sumnow += nums[i]
        #         path.append(nums[i])
        #         backtrack(nums,0)
        #         path.pop()
        #         self.sumnow -= nums[i]
        # backtrack(nums,0)
        # return len(res)

        # 一维DP
        dp = [0]*(target+1)
        dp[0] = 1
        for i in range(target+1):
            for j in nums:
                if i >= j:
                    dp[i]+=dp[i-j]
        return dp[-1]


test = Solution()
nums = [4,2,1]
target = 32
print(test.combinationSum4(nums,target))