def permuteUnique(nums):
    n = len(nums)
    used = [False]*n
    res = []
    nums.sort()
    def backtrack(nums,sol,used):
        if len(sol) == n and sol not in res:
            res.append(sol[:])
        for i in range(n):
            if used[i] == True:
                continue
            else:
                used[i] = True
                sol.append(nums[i])
                backtrack(nums,sol,used)
                sol.pop()
                used[i] = False
    backtrack(nums,[],used)
    return res

nums = [1,1,2]
print(permuteUnique(nums))