class Solution:
    def partition(self, s):
        # 判断回文
        def is_huiwen(s, start, end):
            i = start
            j = end
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        res = []
        path = []
        def backtrack(s,startindex):
            if startindex == len(s):
                res.append(path[:])
                return
            for i in range(startindex,len(s)):
                # 是否添加
                if is_huiwen(s, startindex, i):
                    path.append(s[startindex:i+1])
                    backtrack(s,i+1)
                    path.pop()
                else:
                    continue
        backtrack(s,0)
        return res


test = Solution()
s = "aab"
print(test.partition(s))