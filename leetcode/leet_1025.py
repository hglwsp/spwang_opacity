def divisorGame(n):
    # 选出任一x，满足0 < x < N
    # 且N % x == 0 。
    # 用N - x替换黑板上的数字N 。
    dp = [False] * (n+1)
    dp[1] = False
    for i in range(2,n+1):
        for j in range(1,i):
            if i%j==0 and dp[i-j] == False:
                dp[i] = True
    return dp[n]




test = 3
print(divisorGame(test))