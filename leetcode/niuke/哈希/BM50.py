def twoSum(numbers, target):
    res = []
    hash = dict()
    for i in range(len(numbers)):
        k = target - numbers[i]
        if k not in hash:
            hash[numbers[i]] = i
        else:
            res.append(hash[k] + 1)
            res.append(i+1)
            break
    return res

numbers = [3,2,4]
target = 6
print(twoSum(numbers,target))