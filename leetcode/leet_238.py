def productExceptSelf(nums):
    l = len(nums)
    a = [0] * l
    b = [0] * l
    c = [0] * l
    left = 1
    for i in range(0,l):
        b[i] = left
        left = left * nums[i]
    right = nums[-1]
    for j in range(l-2,-1,-1):
        c[j] = right
        right = right * nums[j]
    c[-1] = 1
    for k in range(0,l):
        a[k] = b[k] * c[k]
    return a


test = [1,2,3,4]
print(productExceptSelf(test))
