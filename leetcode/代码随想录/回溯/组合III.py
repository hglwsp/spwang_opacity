class Solution:
    def combinationSum3(self,k, n):
        res = []
        path = []
        self.sumnow = 0
        # k len   n target
        def backtrack(k,n,startindex):
            # 剪枝，return
            if self.sumnow > n:
                return
            if len(path) == k:
                if self.sumnow == n:
                    res.append(path[:])
                return
            for i in range(startindex,10):
                path.append(i)
                self.sumnow+=i
                backtrack(k,n,i+1)
                path.pop()
                self.sumnow-=i
        backtrack(k,n,1)
        return res

k,n = 3,9
test = Solution()
print(test.combinationSum3(k,n))
