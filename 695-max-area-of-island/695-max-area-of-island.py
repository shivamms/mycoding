class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def checkIsland(r, c, curArea):
            grid[r][c] = 0
            curArea += 1
            if r+1 <= n-1 and grid[r+1][c] == 1:
                curArea = checkIsland(r+1, c, curArea)
            if r-1 >= 0 and grid[r-1][c] == 1:
                curArea = checkIsland(r-1, c, curArea)
            if c+1 <= m-1 and grid[r][c+1] == 1:
                curArea = checkIsland(r, c+1, curArea)
            if c-1 >= 0 and grid[r][c-1] == 1:
                curArea = checkIsland(r, c-1, curArea)
            return curArea
        
        n, m = len(grid), len(grid[0])
        area = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    area = max(area, checkIsland(i, j, 0))
        return area