# 杨辉三角II
# 返回「杨辉三角」的第 rowIndex 行
# input:rowIndex = 3  output:[1,3,3,1]

def getRow(rowIndex):
    ret = list()
    for i in range(0,rowIndex + 1):
        row = list()
        for j in range(0,i+1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(ret[i - 1][j] + ret[i - 1][j - 1])
        ret.append(row)
    return ret[rowIndex]

rowIndex = 3
print(getRow(rowIndex))