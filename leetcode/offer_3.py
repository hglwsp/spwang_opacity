import numpy as np
def findRepeatNumber(nums):
    nums_res = set()
    for num in nums:
        if num in nums_res:
            return num
        else:
            nums_res.add(num)

nums = [1,1,1]
print(findRepeatNumber(nums))