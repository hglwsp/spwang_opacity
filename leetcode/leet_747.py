def dominantIndex(nums):
    res = [0] * len(nums)
    for i in range(0,len(nums)):
        res[i] = nums[i]
    res.sort()
    if res[-1] < res[-2] * 2:
        return -1
    else:
        return nums.index(res[-1])

nums = [3,6,1,0]
print(dominantIndex(nums))