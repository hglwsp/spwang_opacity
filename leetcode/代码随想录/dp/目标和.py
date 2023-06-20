class Solution:
    def findTargetSumWays(self, nums, target):
        # dp
        # sumall = sum(nums)
        # if sumall < abs(target) or (sumall+target) % 2!=0:
        #     return 0
        # n = len(nums)
        # tar = (target + sumall)//2
        # dp = [[0]*(tar+1) for _ in range(n+1)]
        # for a in range(n+1):
        #     dp[a][0] = 1
        # for b in range(1,tar+1):
        #     dp[0][b] = 0
        # for i in range(1,n+1):
        #     for j in range(0,tar+1):
        #         if j < nums[i-1]:
        #             dp[i][j] = dp[i-1][j]
        #         else:
        #             dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i-1]]
        # return dp[-1][-1]
        # dfs
        sumall = sum(nums)
        if sumall < abs(target) or (sumall+target) % 2!=0:
            return 0
        self.sumnow = 0
        res = []
        path = []
        tar = (sumall + target)//2
        nums.sort()
        def backtrack(nums,startindex):
            if self.sumnow == tar:
                res.append(path[:])
                return
            if self.sumnow > tar:
                return
            for i in range(startindex,len(nums)):
                self.sumnow+=nums[i]
                path.append(nums[i])
                backtrack(nums,i+1)
                self.sumnow-=nums[i]
                path.pop()
        backtrack(nums,0)
        return len(res)


test = Solution()
nums = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
target = 0
print(test.findTargetSumWays(nums,target))