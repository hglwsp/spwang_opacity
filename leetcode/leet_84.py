def largestRectangleArea(heights):
    # heights = [0] + heights + [0]
    # n = len(heights)
    # # 单调栈
    # stack = []
    # res = 0
    # for i in range(n):
    #     while stack and heights[stack[-1]] > heights[i]:
    #         tmp = stack.pop()   # 弹出
    #         res = max(res, heights[tmp] * (i - stack[-1] - 1))   # 计算当前柱子为顶最大面积
    #     stack.append(i)
    # return res

    n = len(heights)
    pre,post = [0]*n,[0]*n
    stackpre,stackpost = [],[]
    # 前一个更小
    for i in range(n-1,-1,-1):
        while stackpre and heights[stackpre[-1]]>heights[i]:
            pre[stackpre.pop(-1)] = i+1
        stackpre.append(i)
    for vpre in stackpre:
        pre[vpre] = stackpre[-1]

    # 后一个大
    for j in range(n):
        while stackpost and heights[stackpost[-1]]>heights[j]:
            post[stackpost.pop(-1)]  = j-1
        stackpost.append(j)
    for vpost in stackpost:
        post[vpost] = stackpost[-1]

    ans = 0
    for k in range(n):
        ans = max(ans, heights[k] * (post[k] - pre[k] + 1))
    return ans


heights = [2,1,5,6,2,3]
print(largestRectangleArea(heights))