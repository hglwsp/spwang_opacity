def satcondition(arr,sums,time,n):
    l = 0
    r = len(arr)-1
    left = len(arr)
    while (l<=r):
        m = (l+r)//2
        if arr[m]>time:
            left = m
            r = m-1
        else:
            l = m+1
    n -= len(arr)-left
    rest = left if (left== 0) else sums[left-1]
    return time * n <= rest


def maxRunTime(n, batteries):
    sums = [0] * len(batteries)
    l = len(batteries)
    sums[0] = batteries[0]
    batteries.sort()
    for i in range(1,l):
        sums[i] = sums[i-1]+batteries[i]
    l = 0
    r = sums[-1]/n
    ans = -1
    while (l<=r):
        flag1 = (l+r)//2
        if satcondition(batteries,sums,flag1,n) == True:
            ans = flag1
            l = flag1+1
        else:
            r = flag1-1
    return ans
# def maxRunTime(n, batteries):
#     l = 0
#     r = sum(batteries)//n
#     while l < r:
#         x = (l+r+1)//2
#         if (n*x) <= sum(min(b,x) for b in batteries):
#             l = x
#         else:
#             r = x - 1
#     return l


n = 3
batteries = [10,10,3,5]
print(maxRunTime(n,batteries))

