class Solution:
    def numTrees(self, n):
        if n == 0:return 1
        if n == 1:return 1
        if n == 2:return 2
        dp = [0]*(n+1)
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2
        for i in range(3,n+1):
            for j in range(1,i+1):
                # left 0 -> i 个节点
                dp[i]+= dp[j-1]*dp[i-j]
        return dp[n]

n = 3
test = Solution()
print(test.numTrees(n))