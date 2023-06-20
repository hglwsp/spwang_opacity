def Find(target, array):
    # 数组特殊结构
    if len(array) == 0:
        return False
    if len(array[0]) == 0:
        return False
    m = len(array)
    n = len(array[0])
    i = m-1
    j = 0
    while i >= 0 and j < m:
        if array[i][j] == target:
            return True
        elif array[i][j] > target:
            i-=1
        elif array[i][j] < target:
            j+=1
    return False