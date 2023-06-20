class Solution:
    def subsetsWithDup(self, nums):
        res = []
        path = []
        nums.sort()
        def backtrack(nums,startindex):
            if path not in res:
                res.append(path[:])
            if startindex == len(nums):
                return
            for i in range(startindex,len(nums)):
                path.append(nums[i])
                backtrack(nums,i+1)
                path.pop()
        backtrack(nums,0)
        return res

test = Solution()
nums = [1,2,2]
print(test.subsetsWithDup(nums))