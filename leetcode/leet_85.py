def maximalRectangle(matrix):
    if not matrix: return 0
    m,n = len(matrix), len(matrix[0])
    # 当前位置上方连续1的个数
    # 如第二行（下标从0开始）pre[2]=[3,1,3,2,2,0]，最后多一个0便于单调栈处理
    pre = [0] * (n+2)   # 动态更新
    res = 0
    for i in range(m):
        for j in range(n):
            pre[j] = pre[j] + 1 if matrix[i][j] == "1" else 0
        # 单调栈   pre[0:5]
        stack = [-1]
        for k, num in enumerate(pre):
            while stack and pre[stack[-1]] > num:
                index = stack.pop()
                res = max(res,pre[index]*(k-stack[-1]-1))    # 更新结果
            stack.append(k)
    return res

matrix = [["1","0","1","0","0"],["1","0","1","1","1"],
          ["1","1","1","1","1"],["1","0","0","1","0"]]
print(maximalRectangle(matrix))