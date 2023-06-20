class Solution:
    def restoreIpAddresses(self, s):
        # res = []
        # def is_valid(s,start,end):
        #     if start > end: return False
        #     # 若数字是0开头，不合法
        #     if s[start] == '0' and start != end:
        #         return False
        #     if not 0 <= int(s[start:end + 1]) <= 255:
        #         return False
        #     return True
        # def backtrack(s,startindex,pointsum):
        #     if pointsum == 3:
        #         if is_valid(s,startindex,len(s)-1):
        #             res.append(s[:])
        #             return
        #     for i in range(startindex,len(s)):
        #         if is_valid(s,startindex,i):
        #             s = s[:i+1] + '.' + s[i+1:]
        #             # 加了个点
        #             backtrack(s,i+2,pointsum+1)
        #             s = s[:i+1] + s[i+2:]
        #
        # if len(s) > 12: return []
        # backtrack(s,0,0)
        # return res

        res = []
        path = []
        def is_valid(s, start, end):
            if start > end: return False
            # 若数字是0开头，不合法
            if s[start] == '0' and start != end:
                return False
            if not 0 <= int(s[start:end + 1]) <= 255:
                return False
            return True
        def backtrack(s,startindex):
            if len(path) == 4:
                if startindex == len(s):
                    res.append('.'.join(path[:]))
                    return
            for i in range(startindex,len(s)):
                if is_valid(s,startindex,i):
                    path.append(s[startindex:i+1])
                    backtrack(s,i+1)
                    path.pop()
                else:
                    continue
        backtrack(s,0)
        return res


s = "25525511135"
test = Solution()
print(test.restoreIpAddresses(s))


