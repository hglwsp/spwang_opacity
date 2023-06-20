class Solution:
    def permuteUnique(self, nums):
        res = []
        path = []
        used = [False]*len(nums)
        def backtrack(nums,used):
            if len(path) == len(nums) and path not in res:
                res.append(path[:])
                return
            for i in range(0,len(nums)):
                if used[i] == True:
                    continue
                used[i] = True
                path.append(nums[i])
                backtrack(nums,used)
                path.pop()
                used[i] = False
        backtrack(nums,used)
        return res
test = Solution()
nums = [1,1,2]
print(test.permuteUnique(nums))