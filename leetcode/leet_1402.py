def maxSatisfaction(satisfaction):
    n = len(satisfaction)
    satisfaction.sort(reverse = True)
    if satisfaction[0] <= 0:
        return 0
    dp = [0] * n
    # time[i]*satisfaction[i]
    dp[0] = satisfaction[0]
    temp = 0
    for i in range(1,n):
        temp += satisfaction[i-1]
        dp[i] = dp[i-1] + temp + satisfaction[i]
    return max(dp)

satisfaction = [-1,-8,0,5,-9]
print(maxSatisfaction(satisfaction))