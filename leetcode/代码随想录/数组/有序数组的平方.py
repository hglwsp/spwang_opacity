class Solution:
    def sortedSquares(self, nums):
        n = len(nums)
        res = [0]*n
        l,r,k = 0,n-1,n-1
        while l <= r:
            lm = nums[l]**2
            rm = nums[r]**2
            if lm > rm:
                res[k] = lm
                l+=1
                k-=1
            else:
                res[k] = rm
                r-=1
                k-=1
        return res

test = Solution()
nums = [-4,-1,0,3,10]
print(test.sortedSquares(nums))
