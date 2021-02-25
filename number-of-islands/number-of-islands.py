class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        nIlands = 0
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    nIlands += 1
                    self.dfs(grid, i,j)
        return nIlands
    
    def dfs(self, grid, i , j):
        m = len(grid)
        n = len(grid[0])

        grid[i][j] = "0"

        if i-1 >= 0 and grid[i-1][j] == "1":
            self.dfs(grid, i-1, j)
        if i+1 < m and grid[i+1][j] == "1":
            self.dfs(grid, i+1, j)
        if j-1 >= 0 and grid[i][j-1] == "1":
            self.dfs(grid, i, j-1)
        if j+1 < n and grid[i][j+1] == "1":
            self.dfs(grid, i, j+1)