def findDuplicate(nums):
    # 哈希表,额外空间
    # hash = dict()
    # for i in range(len(nums)):
    #     if nums[i] not in hash:
    #         hash[nums[i]] = i
    #     else:
    #         return nums[i]

    # (n+1)个整数，[1,n]

    # 二分
    n = len(nums)
    left = 0
    right = n
    while left < right:
        mid = left + (right-left)//2
        cnt = sum(num <= mid for num in nums)
        if cnt <= mid:
            left = mid+1
        else:
            right = mid
    return left

nums = [1,3,4,2,2]
print(findDuplicate(nums))