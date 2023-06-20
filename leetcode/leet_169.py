def majorityElement(nums):
    nums.sort()
    l = len(nums)
    return nums[l//2]

test = [2,2,1,1,1,2,2]
print(majorityElement(test))