def nextPermutation(nums):
    # 我们需要将一个左边的「较小数」与一个右边的「较大数」交换，以能够让当前排列变大，从而得到下一个排列。
    #
    # 同时我们要让这个「较小数」尽量靠右，而「较大数」尽可能小。当交换完成后，「较大数」
    # 右边的数需要按照升序重新排列。这样可以在保证新排列大于原来排列的情况下，使变大的幅度尽可能小。
    n = len(nums)
    if n <= 1: return

    modify = -1
    # 从后往前寻找非升序数组的第一个元素对应的下标modify
    for i in range(n - 1, -1, -1):
        if i == n - 1: continue
        if nums[i] < nums[i + 1]:
            modify = i
            break

    # 如果modify没变，则此时排列为最大，将数组逆序
    if modify == -1:
        nums[:] = nums[::-1]

    # 否则
    else:
        target = -1
        # 找到modify之后比modify大且最接近的元素的下标target
        for i in range(n - 1, modify, -1):
            if nums[i] > nums[modify]:
                target = i
                break

        # 将modify和target位置的元素交换
        nums[modify], nums[target] = nums[target], nums[modify]

        # 将modify位置之后的元素倒序
        i, j = modify + 1, n - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i, j = i + 1, j - 1





nums = [1,2,3]
print(nextPermutation(nums))

