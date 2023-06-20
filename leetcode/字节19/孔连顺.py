n = int(input())    # buildings
d = int(input())    # maxdistance between two humans
nums = [0]*n
for i in range(n):
    nums[i] = int(input())   # locations of buildings
res = 0
# print(n)
# print(d)
# print(nums)
# double links
nums.sort()
slow = 0
fast = 2
while fast < n:
    if (fast - slow < 2):
        fast+=1
    elif nums[fast] - nums[slow] <= d:
        res+= (fast-slow-1)*(fast-slow)/2
        fast+=1
    elif nums[fast] - nums[slow] > d:
        slow+=1
print(res%99997867)
