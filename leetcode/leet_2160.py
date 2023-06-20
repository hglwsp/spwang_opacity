def minimumSum(num):
    nums = []
    while num!=0:
        nums.append(num%10)
        num//=10
    nums.sort()
    res = 10*(nums[0]+nums[1])+nums[2]+nums[3]
    return res

num = 2932
print(minimumSum(num))
