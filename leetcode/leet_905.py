def sortArrayByParity(nums):
    l = len(nums)
    res_ji = []
    res_ou = []
    for i in range(0,l):
        if nums[i] % 2 == 0:
            res_ou.append(nums[i])
        else:
            res_ji.append(nums[i])
    for j in range(0,len(res_ji)):
        res_ou.append(res_ji[j])
    return res_ou

nums = [3,1,2,4]
print(sortArrayByParity(nums))
