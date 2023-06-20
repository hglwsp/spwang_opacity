def removeDuplicates(nums):
    a = 0
    b = 1
    while b < len(nums):
        if nums[b] == nums[a]:
            b += 1
        else:
            a += 1
            nums[a] = nums[b]
    return a + 1


test = [1,1,2]
print(removeDuplicates(test))