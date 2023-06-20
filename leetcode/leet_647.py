def countSubstrings(s):
    # dp
    # n = len(s)
    # dp = [[False]*n for _ in range(n)]
    # ans = 0
    # for i in range(n-1,-1,-1):
    #     for j in range(i,n):
    #         if s[i] == s[j]:
    #             if i==j or j-i == 1:
    #                 dp[i][j] = True
    #                 ans+=1
    #             elif dp[i+1][j-1]:  # bb -> abba
    #                 dp[i][j] = True
    #                 ans+=1
    # return ans

    # 中心
    n,ans = len(s),0
    for i in range(0,2*n+1):
        l,r = i//2,i//2+i%2
        while l>=0 and r<n and s[l]==s[r]:
            l-=1
            r+=1
            ans+=1
    return ans