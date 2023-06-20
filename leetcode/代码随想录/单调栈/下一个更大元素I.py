class Solution:
    # nums1 是 nums2 的子集
    def nextGreaterElement(self, nums1, nums2):
        res = [-1]*len(nums1)
        stack = [0]
        for i in range(1,len(nums2)):
            if nums2[i] <= nums2[stack[-1]]:
                stack.append(i)
            else:
                while len(stack)!=0 and nums2[i] > nums2[stack[-1]]:
                    if nums2[stack[-1]] in nums1:
                        index = nums1.index(nums2[stack[-1]])
                        res[index] = nums2[i]
                    stack.pop()
                stack.append(i)
        return res