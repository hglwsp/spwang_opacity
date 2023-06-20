# class Solution:
#     def subsets(self, nums):
#         r = 0
#         res = []
#         path = []
#         def backtrack(nums):
#             # 收集子集，要放在终止添加的上面，否则会漏掉自己
#             res.append(path[:])
#             if nums == 0:
#                 return
#             for i in range(1,4):
#                 path.append(i)
#                 if nums - i > 0 and (nums-i)%3 != 0:
#                     backtrack(nums - i)
#                 path.pop()
#         backtrack(nums)
#         for i in range(len(res)):
#             if sum(res[i]) == n:
#                 r+=1
#         return r
#
# test = Solution()
# n = int(input())
# print(test.subsets(n+1))

n = int(input())
dp = [0]*(n+1)
dp[0] = 0
dp[1] = 1
dp[2] = 2
for i in range(3,n+1):
    if i%3 == 0:
        dp[i] = 0
    else:
        dp[i] = dp[i-1]+dp[i-2]+dp[i-3]
print(dp[-1])