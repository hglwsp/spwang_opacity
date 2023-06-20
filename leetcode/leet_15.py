def threeSum(nums):
    # 给你一个包含n个整数的数组nums，判断nums中是否存在三个元素a，b，c ，使得a + b + c = 0 ？请你找出所有和为0且不重复的三元组。
    nums.sort()
    n = len(nums)
    res = []
    if (n < 3):
        return []
    for i in range(0,n):
        if (nums[i] > 0):
            return res
        l = i+1
        r = n-1    # 双指针
        if (i > 0 and nums[i] == nums[i - 1]):
            continue
        while (l < r):
            if nums[i] + nums[l] + nums[r] == 0:
                res.append([nums[i],nums[l],nums[r]])
                while (nums[l] == nums[l+1] and l < r): #(l<r and nums[l]==nums[l+1])
                    l+=1
                while (nums[r] == nums[r-1] and l < r):
                    r-=1
                l+=1
                r-=1         # 跳出重复元素
            elif nums[i] + nums[l] + nums[r] < 0:
                l+=1
            elif nums[i] + nums[l] + nums[r] > 0:
                r-=1
    return res

nums = [0,0,0]
# -4,-1,-1,0,1,2
print(threeSum(nums))