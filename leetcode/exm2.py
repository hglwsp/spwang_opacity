def sort(nums):
    nums_di = filter(str.isdigit,nums)
    l = len(nums_di)
    nums_sort = sorted(nums,reverse=True)
    nums_sort_d = []
    for i in range(0,l):
        if nums_sort[i]%2==0:
            nums_sort_d.append(nums_sort[i])
    return nums_sort_d

test = 'adasdasdas463215das'
print(sort(test))

