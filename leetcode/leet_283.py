def moveZeroes(nums):
    l = len(nums)
    sum = 0     #0的个数
    for i in range(0,l):
        if nums[i] == 0:
            sum+=1
    while 0 in nums:
        nums.remove(0)
    for j in range(0,sum):
        nums.append(0)
    return nums


test = [0,1,0,3,12]
print(moveZeroes(test))