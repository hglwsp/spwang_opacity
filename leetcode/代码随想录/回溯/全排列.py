class Solution:
    # 每层都是从0开始搜索而不是startIndex
    # 需要used数组记录path里都放了哪些元素了
    def permute(self, nums):
        res = []
        path = []
        used = [False] * len(nums)
        def backtrack(nums,used):
            if len(path) == len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                # 已选
                if used[i] == True:
                    continue
                used[i] = True
                path.append(nums[i])
                backtrack(nums,used)
                path.pop()
                used[i] = False   # 撤销选择
        backtrack(nums,used)
        return res
test = Solution()
nums = [1,2,3]
print(test.permute(nums))