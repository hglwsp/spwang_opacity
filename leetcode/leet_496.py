def nextGreaterElement(nums1, nums2):
    l1 = len(nums1)
    l2 = len(nums2)
    flag = []
    a = []
    for i in range(0,l1):
        for j in range(0,l2):
            if nums1[i] == nums2[j]:
                flag.append(j)
    for m in range(0,l1):
        n = flag[m] + 1
        while n < l2 and nums2[n] < nums1[m]:
            n+=1
        if n<l2:
            a.append(nums2[n])
        else:
            a.append(-1)
    return a
nums1 = [4,1,2]
nums2 = [1,3,4,2]
print(nextGreaterElement(nums1,nums2))