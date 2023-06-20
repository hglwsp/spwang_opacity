class Solution:
    def minSubArrayLen(self, target, nums):
        # special case
        n = len(nums)
        if n==1 and nums[0] < target:
            return 0
        elif n==1 and nums[0] > target:
            return 1
        elif sum(nums) < target:
            return 0
        else:
            start,end = 0,0
            minlength = n+1
            total = 0
            while end<n:
                total += nums[end]
                while total >= target:
                    minlength = min(minlength,end - start + 1)
                    total-=nums[start]
                    start+=1
                end+=1
            return minlength

test = Solution()
target = 7
nums = [2,3,1,2,4,3]
print(test.minSubArrayLen(target,nums))