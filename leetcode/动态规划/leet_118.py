# 杨辉三角
#给定一个非负整数 numRows，生成「杨辉三角」的前 numRows 行。
#在「杨辉三角」中，每个数是它左上方和右上方的数的和。
# input:numRows = 5 output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
#     1
#    1 1
#   1 2 1
#  1 3 3 1
# 1 4 6 4 1
# dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

def generate(numRows):
    ret = list()
    for i in range(0,numRows):
        row = list()
        for j in range(0,i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(ret[i-1][j] + ret[i-1][j-1])
        ret.append(row)
    return ret

numRows = 5
print(generate(numRows))
