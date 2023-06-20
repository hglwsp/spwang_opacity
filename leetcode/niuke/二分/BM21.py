def minNumberInRotateArray(rotateArray):
    n = len(rotateArray)
    if n == 1:
        return rotateArray[0]

    l = 0
    r = n-1
    while l <= r:
        mid = (l + r)//2
        if rotateArray[mid] > rotateArray[r]:   # 右半部
            l = mid + 1
        elif rotateArray[mid] > rotateArray[l]:  # 左半部
            r = mid - 1
        else:
            r -= 1
    return rotateArray[l]
