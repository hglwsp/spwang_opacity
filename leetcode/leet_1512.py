def numIdenticalPairs(nums):
    # 如果一组数字(i, j)满足nums[i] == nums[j]且i < j ，就可以认为这是一组好数对。
    res = 0        # result
    l = len(nums)
    for i in range(0,l-1):
        for j in range(i+1,l):
            if nums[i] == nums[j]:   # nums[i] == nums[j]且i < j
                res+=1
    return res

nums = [1,2,3,1,1,3]
print(numIdenticalPairs(nums))