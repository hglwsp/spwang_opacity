def isMatch(s, p):
    m,n = len(s),len(p)
    dp = [[False]*(n+1) for _ in range(m+1)]
    dp[0][0] = True
    # *不会是第一个 .万能，*多个或0个
    for i in range(2,n+1):
        if p[i-1] == '*':
            dp[0][i] = dp[0][i-2]
    for a in range(1,m+1):
        for b in range(1,n+1):
            if s[a-1] == p[b-1] or p[b-1] == '.':
                dp[a][b] = dp[a-1][b-1]
            elif p[b-1] == '*':
                if s[a-1]!=p[b-2] and p[b-2]!='.':
                    # 只能是0
                    dp[a][b] = dp[a][b-2]
                else:
                    dp[a][b] = dp[a][b-2] or dp[a-1][b]
                        # 0个 多个
    return dp[m][n]

s = "aa"
p = "a*"
print(isMatch(s,p))
