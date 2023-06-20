class Solution:
    def lastStoneWeightII(self, stones):
        sumall,n = sum(stones),len(stones)
        target = sumall // 2
        dp = [[False]*(target+1) for _ in range(n+1)]
        dp[0][0] = True
        for i in range(1,n+1):
            for j in range(0,target+1):
                if j < stones[i-1]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-stones[i-1]]
        ans = sumall
        for b in range(target+1):
            if dp[n][b]:
                tmp = sumall - 2*b
                ans = min(ans,tmp)
        return ans

stones = [31,26,33,21,40]`
test = Solution()
print(test.lastStoneWeightII(stones))