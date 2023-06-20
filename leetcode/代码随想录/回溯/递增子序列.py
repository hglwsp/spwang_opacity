class Solution:
    def findSubsequences(self, nums):
        res = []
        path = []
        def backtrack(nums,startindex):
            if len(path) >= 2:
                res.append(path[:])
            if startindex == len(nums):
                return
            used = set() # 新的一层uset都会重新定义（清空），所以要知道uset只负责本层！
            for i in range(startindex,len(nums)):
                if nums[i] in used or (path and nums[i] < path[-1]):   # path 不能是空
                    continue
                used.add(nums[i])
                path.append(nums[i])
                backtrack(nums,i+1)
                path.pop()
        backtrack(nums,0)
        return res

nums = [4,6,7,7]
test = Solution()
print(test.findSubsequences(nums))


