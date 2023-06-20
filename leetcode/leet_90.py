def subsetsWithDup(nums):
    res = []
    nums.sort()
    def backtrack(sol,nums,index):
        if index == len(nums) and sol not in res:
            res.append(sol)
            return
        # select / not select
        for i in range(index,len(nums)):
            if i > index and nums[i] == nums[i-1]:
                continue
            backtrack(sol, nums, i + 1)
            backtrack(sol+[nums[index]],nums,i+1)
    backtrack([],nums,0)
    return res



nums = [1,2,3,4,5,6,7,8,10,0]
print(subsetsWithDup(nums))