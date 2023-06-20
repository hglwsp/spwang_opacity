class Solution:
    def solveSudoku(self, board):
        def is_valid(row,col,val,board):
            # 行
            for i in range(9):
                if board[row][i] == str(val):
                    return False
            for j in range(9):
                if board[j][col] == str(val):
                    return False
            # 判断同一九宫格是否有冲突
            start_row = (row // 3) * 3
            start_col = (col // 3) * 3
            for i in range(start_row, start_row + 3):
                for j in range(start_col, start_col + 3):
                    if board[i][j] == str(val):
                        return False
            return True

        def backtrack(board):
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] != '.':
                        continue
                    for k in range(1,10):
                        if is_valid(i,j,k,board):
                            board[i][j] = str(k) # 放置k
                            if backtrack(board): # 如果找到合适一组立刻返回
                                return True
                            board[i][j] = '.'   # 回溯，撤销k
                    # 1-9 都不能填入
                    return False
            return True
        backtrack(board)