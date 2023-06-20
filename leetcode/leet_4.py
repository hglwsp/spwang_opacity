def findMedianSortedArrays(nums1, nums2):
    l1 = len(nums1)
    l2 = len(nums2)
    l = l1 + l2
    res = []
    for i in range(0,l1):
        res.append(nums1[i])
    for j in range(0,l2):
        res.append(nums2[j])
    res.sort()
    if l % 2 == 1:
        return res[l//2]
    else:
        return (res[l//2] + res[l//2 - 1]) / 2

nums1 = [1,3]
nums2 = [2]
print(findMedianSortedArrays(nums1,nums2))