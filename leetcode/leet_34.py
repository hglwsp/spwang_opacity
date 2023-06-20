def searchRange( nums, target):
    l = len(nums)
    a = []
    for i in range(l):
        if nums[i] == target:
            a.append(i)
    if a == []:
        return [-1,-1]
    elif len(a) == 1:
        return [a[0],a[0]]
    else:
        return [a[0],a[-1]]

nums = [5,7,7,8,8,10]
target = 8
print(searchRange(nums,target))