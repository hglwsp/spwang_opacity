def findMaxConsecutiveOnes(nums):
    n = len(nums)
    res,cur = 0,0
    for i in range(0,n):
        if nums[i] == 1:
            cur += 1
        else:
            res = max(res, cur)
            cur = 0
    res = max(res,cur)
    return res

nums = [1,1,0,1,1,1]
print(findMaxConsecutiveOnes(nums))