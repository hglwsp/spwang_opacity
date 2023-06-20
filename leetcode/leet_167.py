def twoSum(numbers, target):
    low = 0
    high = len(numbers) - 1
    while low < high:
        sum = numbers[low] + numbers[high]
        if sum < target:
            low += 1
        elif sum == target:
            return [low+1,high+1]
        else:
            high -= 1
    return [-1,-1]

numbers = [2,3,4]
target = 6
print(twoSum(numbers,target))
