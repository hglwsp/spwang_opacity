def combine(n, k):
    res = [] # #存放符合条件结果的集合
    path = [] #用来存放符合条件结果
    def dfs(n,k,startindex):
        if len(path) == k:
            res.append(path[:])
            return
        for i in range(startindex,n+1):
            path.append(i)
            dfs(n,k,i+1)
            path.pop()
    dfs(n,k,1)
    return res

n,k = 4,2
print(combine(n, k))

