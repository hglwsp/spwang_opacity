class Solution:
    def solveNQueens(self, n):
        # 不能同行     不能同列     不能同斜线
        if not n:
            return []
        board = [['.'] * n for _ in range(n)]
        res = []
        def is_valid(board,row,col):
            # col
            for i in range(len(board)):
                if board[i][col] == 'Q':
                    return False
            # 斜线 45 左上
            i = row-1
            j = col-1
            while i>=0 and j>=0:
                if board[i][j] == 'Q':
                    return False
                i-=1
                j-=1
            # 斜线 135 右上
            i = row-1
            j = col+1
            while i<len(board) and j<len(board[0]):
                if board[i][j] == 'Q':
                    return False
                i-=1
                j+=1
            return True

        def backtrack(board,row,n):
            # 终止条件
            if row == n:
                temp_res = []
                for temp in board:
                    temp_str = "".join(temp)
                    temp_res.append(temp_str)
                res.append(temp_res)
            for col in range(n):
                if not is_valid(board,row,col):
                    continue
                board[row][col] = 'Q'
                backtrack(board,row+1,n)
                board[row][col] = '.'
        backtrack(board,0,n)
        return res

n = 4
test = Solution()
print(test.solveNQueens(n))



