def longestPalindrome(s):
    # 中心扩展
    # n,res = len(s),[]
    # for i in range(0,2*n+1):
    #     l,r = i//2,i//2+i%2
    #     while l>=0 and r<n and s[l]==s[r]:
    #         res.append(s[l:r+1])
    #         l-=1
    #         r+=1
    # result = res[0]
    # for index in range(0,len(res)):
    #     if len(res[index]) > len(result):
    #         result = res[index]
    # return result

    # dp
    n = len(s)
    dp = [[False]*n for _ in range(n)]
    for i in range(n-1,-1,-1):
        for j in range(i,n):
            if s[i] == s[j]:
                if i==j or j-i==1:
                    dp[i][j] = True
                elif dp[i+1][j-1]:
                    dp[i][j] = True
    start,end,length = 0,0,0
    for a in range(n):
        for b in range(n):
            if dp[a][b] == True and length < (b-a+1):
                length = b-a+1
                start = a
                end = b
    return s[start:end+1]

s = "babad"
print(longestPalindrome(s))