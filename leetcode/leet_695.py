def maxAreaOfIsland(self,grid):
    def dfs(grid,r,c):
        if not 0<=r<len(grid) or not 0<=c<len(grid[0]):return
        if grid[r][c]!=1 : return
        grid[r][c] = 2
        self.S+=1
        dfs(grid,r-1,c)
        dfs(grid,r+1,c)
        dfs(grid,r,c-1)
        dfs(grid,r,c+1)

    res = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                self.S = 0
                dfs(grid,i,j)
                res = max(res,self.S)
    return res

grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]]

print(maxAreaOfIsland(grid))