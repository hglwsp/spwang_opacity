class Solution:
    def letterCombinations(self, digits):
        if not digits:
            return []
        letter_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        res = []
        path = []
        def backtrack(digits,index):
            if index == len(digits):
                # 调整输出方法
                res.append("".join(path))
                return
            digit = digits[index]
            for letter in letter_map[digit]:
                path.append(letter)
                backtrack(digits,index+1)
                path.pop()
        backtrack(digits,0)
        return res

digits = "23"
test = Solution()
print(test.letterCombinations(digits))
