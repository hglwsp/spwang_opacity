def dailyTemperatures(temperatures):
    # n = len(temperatures)
    # ans = []
    # # two loop 超时
    # for i in range(0,n-1):
    #     for j in range(i+1,n):
    #         if temperatures[i] < temperatures[j]:
    #             ans.append(j-i)
    #             break
    #         # bound
    #         if j == n-1 and temperatures[i] >= temperatures[j]:
    #             ans.append(0)
    # # last day
    # ans.append(0)
    # return ans

    # 单调栈
    n = len(temperatures)
    res = [0]*n
    stack = []
    for i in range(n):
        while stack and temperatures[i]>temperatures[stack[-1]]:
            index = stack.pop()
            res[index] = i - index
        stack.append(i)
    return res

temperatures = [34,80,80,80,34,80,80,80,34,34]
print(dailyTemperatures(temperatures))