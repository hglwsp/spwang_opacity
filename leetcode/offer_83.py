def permute(nums):
    n = len(nums)
    res = []
    used = [False] * n
    def backtrack(nums,sol,used):
        if len(sol) == n:
            res.append(sol[:])
            return
        else:
            for i in range(n):
                if used[i]:
                    continue
                # 选择
                sol.append(nums[i])
                used[i] = True
                backtrack(nums,sol,used)
                sol.pop()
                used[i] = False
    backtrack(nums,[],used)
    return res

nums = [1,2,3]
print(permute(nums))

