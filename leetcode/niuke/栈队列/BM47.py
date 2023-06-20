def findKth(self,a, n, K):
    res = self.quicksort(a)
    return res[n-K]

def quicksort(self,arr):
    if len(arr) >= 2:
        mid = arr[len(arr)//2]    # 标杆
        left = []
        right = []
        arr.remove(mid)
        for num in arr:
            if num > mid:
                right.append(num)
            else:
                left.append(num)
        return self.quicksort(left) + [mid] + self.quicksort(right)
    else:
        return arr