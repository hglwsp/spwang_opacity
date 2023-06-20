def findKthLargest(nums, k):
    nums_d = list(set(nums))
    nums_d.sort()
    return nums_d[-k]


nums =[3,2,3,1,2,4,5,5,6]
k = 4
print(findKthLargest(nums,k))