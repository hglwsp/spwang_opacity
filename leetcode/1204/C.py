n,k = map(int,input().split(' '))
nums = list(map(int,input().split(' ')))
res = 0
for i in range(n-1):
    if nums[i] > k:
        res += (nums[i] - k + 1)
        nums[i] = k-1
    if nums[i+1] > k:
        res += (nums[i + 1] - k + 1)
        nums[i+1] = k-1
    else:
        if nums[i] + nums[i+1] > k:
            res += (nums[i] + nums[i + 1] - k)
            nums[i + 1] = k - 1
print(nums)
print(res)

