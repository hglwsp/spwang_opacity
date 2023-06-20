# 比特位计数
# 给你一个整数 n ，对于 0 <= i <= n 中的每个 i ，计算其二进制表示中 1 的个数 ，
# 返回一个长度为 n + 1 的数组 ans 作为答案。
# input:n = 2    output:[0,1,1]
# input:n = 5    output:[0,1,1,2,1,2]
# 动态规划——最高有效位
def countBits(n):
    dp = []
    dp.append(0)
    dp.append(1)
    multi = 1
    for i in range(2,n+1):
        if multi * 2 == i:
            dp.append(1)
            multi *= 2
        else:
            dp.append(1 + dp[i - multi])
    return dp

test = 5
print(countBits(test))