def isIdealPermutation(nums):
    # l = len(nums)
    # for i in range(0,l-2):
    #     for j in range(i+2,l):
    #         if nums[i]>nums[j]:
    #             return True
    # return False
    l = len(nums)
    i = 0
    while i < l-1:
        if nums[i] > nums[i+1]:     # change i and i+1
            flag = nums[i]
            nums[i] = nums[i+1]
            nums[i+1] = flag
            i+=2
        else:
            i+=1

    for k in range(0,l-1):     #check sort
        if nums[k]>nums[k+1]:
            return False
    return True

nums = [1,2,0]
print(isIdealPermutation(nums))