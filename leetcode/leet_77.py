def combine(n, k):
    def dfs(sol,i):
        nonlocal ans
        if len(sol) == k:
            ans.append(sol[:])
            return
        if i == n+1:
            return
        dfs(sol+[i],i+1)
        dfs(sol,i+1)
    ans = []
    dfs([],1)
    return ans

n=1
k=1
print(combine(n,k))