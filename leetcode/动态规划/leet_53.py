# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
# input:nums = [-2,1,-3,4,-1,2,1,-5,4]
# output:6
# 转移方程 : f(i)=max{f(i−1)+nums[i],nums[i]}
# 遍历一遍，用两个变量，一个记录最大的和，一个记录当前的和
def maxSubArray(nums):
    # idea1
    # l = len(nums)
    # tmp = nums[0]
    # max_ = tmp
    # for i in range(1,l):
    #     if tmp + nums[i] > nums[i]:
    #         max_ = max(tmp + nums[i],max_)
    #         tmp = tmp + nums[i]
    #     else:
    #         max_ = max(max_, tmp, tmp + nums[i], nums[i])
    #         tmp = nums[i]
    # return max_

    # idea2
    l = len(nums)
    for i in range(1,l):
        nums[i] = max(nums[i-1] + nums[i],nums[i])
    return max(nums)

test = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(test))
