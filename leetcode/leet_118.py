def generate(numRows):
    ret = list()
    for i in range(0,numRows):
        row = list()
        for j in range(0,i+1):
            if j == 0 or j == i :
                row.append(1)         #最两侧是1
            else:
                row.append(ret[i-1][j] + ret[i-1][j-1])
        ret.append(row)
    return ret

test = 5
print(generate(test))