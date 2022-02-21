class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def checkIsland(r, c, curArea):
            visited.add((r,c))
            curArea += 1
            if (r+1, c) not in visited and r+1 <= n-1 and grid[r+1][c] == 1:
                curArea = checkIsland(r+1, c, curArea)
            if (r-1, c) not in visited and r-1 >= 0 and grid[r-1][c] == 1:
                curArea = checkIsland(r-1, c, curArea)
            if (r, c+1) not in visited and c+1 <= m-1 and grid[r][c+1] == 1:
                curArea = checkIsland(r, c+1, curArea)
            if (r, c-1) not in visited and c-1 >= 0 and grid[r][c-1] == 1:
                curArea = checkIsland(r, c-1, curArea)
            return curArea
        
        n, m = len(grid), len(grid[0])
        visited = set()
        area = 0
        for i in range(n):
            for j in range(m):
                if (i,j) not in visited and grid[i][j] == 1:
                    area = max(area, checkIsland(i, j, 0))
        return area