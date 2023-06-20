def singleNumber(nums):
     s = []
     for num in nums:
         if num in s:
             s.remove(num)
         else:
             s.append(num)
     return s


nums = [1,2,1,3,2,5]
print(singleNumber(nums))



