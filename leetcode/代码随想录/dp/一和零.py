class Solution:
    def findMaxForm(self, strs, m, n):
        a = len(strs)
        dp = [[[0]*(n+1) for _ in range(m+1)] for _ in range(a+1)]
        for i in range(1,a+1):
            zeronum = strs[i-1].count('0')
            onenum = strs[i-1].count('1')
            for j in range(m+1):  # 0 的背包容量
                for k in range(n+1): # 1 的背包容量
                    if zeronum > j or onenum > k:
                        dp[i][j][k] = dp[i-1][j][k]
                    else:
                        dp[i][j][k] = max(dp[i-1][j][k],dp[i-1][j-zeronum][k-onenum]+1)
        return dp[a][m][n]
strs = ["10", "0", "1"]
m = 1
n = 1
test = Solution()
print(test.findMaxForm(strs,m,n))


