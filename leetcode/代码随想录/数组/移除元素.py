class Solution:
    def removeElement(self, nums, val):
        # 双指针
        l,r = 0,0
        n = len(nums)
        while l < n:
            if nums[l] != val:
                nums[r] = nums[l]
                r+=1
            l+=1
        return r