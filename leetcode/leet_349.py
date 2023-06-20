def intersection(nums1, nums2):
    l1 = len(nums1)
    l2 = len(nums2)
    a = []
    for i in range(0,l1):
        for j in range(0,l2):
            if(nums1[i] == nums2[j]):         #不考虑重复情况
                a.append(nums1[i])
    a1 = list(set(a))
    return a1

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(intersection(nums1, nums2))