def oddCells( m, n, indices):
    matrix = [[0] * n for _ in range(m)]
    for x,y in indices:
        for j in range(n):
            matrix[x][j] += 1
        for row in matrix:
            row[y] += 1
    return sum(x % 2 for row in matrix for x in row)

m = 2
n = 3
indices = [[0,1],[1,1]]
print(oddCells(m,n,indices))