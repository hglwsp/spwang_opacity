def lexicalOrder(n):
    # 给你一个整数n ，按字典序返回范围[1, n]内所有整数。
    # dfs solve
    def dfs(k,res):
        if k <= n:
            res.append(k)
            t = 10*k
            if t <= n:
                for i in range(10):
                    dfs(t + i, res)
    res = []
    for i in range(1,10):
        dfs(i,res)
    return res


n = 23
print(lexicalOrder(n))

