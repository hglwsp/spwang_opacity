def migong(self,grid):
    # 4*4
    def dfs(grid, r, c):
        if not 0 <= r < len(grid) or not 0 <= c < len(grid[0]): return
        if grid[r][c] != 1: return
        grid[r][c] = 2
        res.append(grid[r][c])
        if grid[r-1][c] == 0:
            dfs(grid, r - 1, c)
        if grid[r+1][c] == 0:
            dfs(grid, r + 1, c)
        if grid[r][c+1] == 0:
            dfs(grid, r, c - 1)
        if grid[r][c - 1] == 0:
            dfs(grid, r, c + 1)
    res = []



