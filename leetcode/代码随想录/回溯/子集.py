class Solution:
    def subsets(self, nums):
        res = []
        path = []
        def backtrack(nums,index):
            # 收集子集，要放在终止添加的上面，否则会漏掉自己
            res.append(path[:])
            if index == len(nums):
                return
            for i in range(index,len(nums)):
                path.append(nums[i])
                backtrack(nums,i+1)
                path.pop()
        backtrack(nums,0)
        return res

test = Solution()
nums = [1,2,3]
print(test.subsets(nums))