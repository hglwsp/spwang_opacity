# 输入：lo = 12, hi = 15, k = 2
# 输出：13
def getKth(lo, hi, k):
    l = hi - lo + 1
    dp = [0]*l
    dp_i = [0]*l
    for j in range(0,l):
        dp_i[j] = j + lo
    for i in range(lo,hi+1):
        step = 0
        wei = i
        while i != 1:
            if i%2 == 0:
                i = i/2
                step+=1
            else:
                i = 3*i + 1
                step+=1
        dp[wei-lo] = step
    flag = dp
    dp.sort()
    for iter in range(0,l):
        if flag[iter] == dp[k-1]:
            break
    return dp_i[iter]

lo = 12
hi = 15
k = 2
print(getKth(lo, hi, k))