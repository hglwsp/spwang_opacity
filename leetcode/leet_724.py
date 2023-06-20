def pivotIndex(nums):
    # 输入：nums = [1, 7, 3, 6, 5, 6]
    # 输出：3
    # 解释：
    # 中心下标是
    # 3 。
    # 左侧数之和
    # sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11 ，
    # 右侧数之和
    # sum = nums[4] + nums[5] = 5 + 6 = 11 ，二者相等。
    # l = len(nums)  # 数组长度
    # #二分法
    # left = 0
    # right = l
    # mid = (right - left)//2
    # while left <= right:
    #     sum_left = 0
    #     sum_right = 0  # 左侧数和右侧数和
    #     for i in range(0,mid):
    #         sum_left+=nums[i]
    #     for j in range(mid+1,l):
    #         sum_right+=nums[j]
    #     if sum_left == sum_right:
    #         return  mid
    #     elif sum_left > sum_right:
    #         right = mid - 1
    #     else:
    #         left = mid + 1
    # return  -1
    # 二分法超时,区间求和想preSum数组
    l = len(nums)
    sums = 0
    preSum = []
    preSum.append(sums)
    for i in range(0,l):
        sums += nums[i]
        preSum.append(sums)            #preSum数组
    lp = len(preSum)      #preSum数组长度
    for j in range(1,lp):
        if preSum[j] == preSum[lp-1] - preSum[j+1]:
            return j
    return -1


test = [1,7,3,6,5,6]
print(pivotIndex(test))

