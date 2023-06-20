class Solution:
    def subsets(self, nums,lenn,lenk):
        res = []
        path = []
        def backtrack(nums,index_n,lenk):
            # 收集子集，要放在终止添加的上面，否则会漏掉自己
            res.append(path[:])
            if index_n == lenn or lenk == 0:
                return
            for i in range(index_n,lenn):
                path.append(nums[i])
                backtrack(nums,i+1,lenk-1)
                path.pop()
        backtrack(nums,0,lenk)
        result = []
        for i in range(len(res)):
            if len(res[i]) == lenk:
                result.append(res[i])
        result.sort()
        flag = 0
        for i in range(len(result)):
            if result[i][0] == 0:
                flag = i
        return result[flag+1]

# input
# 6357924710
# 3
nums = list(map(int,input().split(' ')))
N = len(nums)
K = int(input())

test = Solution()
print(test.subsets(nums,N,K))