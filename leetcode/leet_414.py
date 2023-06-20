def thirdMax(nums):
    nums_set = list(set(nums))
    length = len(nums_set)
    nums_set.sort()
    if length < 3:
        return nums_set[length - 1]
    elif length == 3:
        return nums_set[0]
    else:
        return nums_set[length - 4]

test = [3,2,-1]
print(thirdMax(test))