def subsets(nums):
    res = []
    def backtrack(sol,nums,index):
        n = len(nums)
        if index == n:
            res.append(sol)
            return
        backtrack(sol,nums,index+1)
        backtrack(sol+[nums[index]],nums,index+1)
    backtrack([],nums,0)
    return res

nums = [1,2,3]
print(subsets(nums))
