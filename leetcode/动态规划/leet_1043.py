# 给你一个整数数组 arr，请你将该数组分隔为长度最多为 k 的一些（连续）子数组。
# 分隔完成后，每个子数组的中的所有值都会变为该子数组中的最大值。
# 返回将数组分隔变换后能够得到的元素最大和。

# 输入：arr = [1,15,7,9,2,5,10], k = 3
# dp[0] = 1
# dp[1] = 30
# dp[2] = 45
# dp[3] = max(dp[2]+arr[3],dp[0]+arr[0])
# dp[4] = max(dp[012]+arr[3]+arr[4],dp[123]+arr[0]+arr[4],dp[345]+arr[1]+arr[2])
# dp[n] = max(dp[n], dp[n-i]+max(arr[n], arr[n-i+1])*i);
# 输出：84

def maxSumAfterPartitioning(arr, k):
    n = len(arr)
    dp = [0]*n
    # index < k
    for i in range(k):
        dp[i] = max(arr[:i+1])*(i+1)
    for i in range(k,n):
        poss_solve = []
        for span in range(1,k+1):
            poss_solve.append(dp[i-span]+max(arr[i-span+1:i+1])*span)
        dp[i] = max(poss_solve)
    return dp[-1]

arr = [1,15,7,9,2,5,10]
k = 3
print(maxSumAfterPartitioning(arr,k))
