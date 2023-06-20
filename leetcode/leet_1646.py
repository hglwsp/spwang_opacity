def getMaximumGenerated(n):
#nums[0] = 0
#nums[1] = 1
#2 <= 2 * i <= n 时，nums[2 * i] = nums[i]
#2 <= 2 * i + 1 <= n 时，nums[2 * i + 1] = nums[i] + nums[i + 1]

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        nums = [0] * (n+1)
        # print(nums)
        nums[0] = 0
        nums[1] = 1
        for i in range(2,n+1):
            if i%2 == 0:
                nums[i] = nums[i//2]
            else:
                nums[i] = nums[i//2] + nums[i//2 + 1]
    nums.sort()
    return nums[n-1]


test = 7
print(getMaximumGenerated(test))

