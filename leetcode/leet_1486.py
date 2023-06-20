def xorOperation(n, start):
    nums = []
    for i in range(0,n):
        flag = start + 2 * i
        nums.append(flag)
    res = nums[0]
    for j in range(1,n):
        res = res ^ nums[j]
    return res

n = 5
start = 0
print(xorOperation(n,start))