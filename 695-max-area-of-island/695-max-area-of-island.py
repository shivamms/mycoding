class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        self.currArea = 0
        def areaOfIsland(r, c):
            if r < 0 or r > m-1 or c < 0 or c > n-1 or grid[r][c] == 0:
                return 0
            if grid[r][c] == 1:
                grid[r][c] = 0
                self.currArea += 1
                areaOfIsland(r+1, c)
                areaOfIsland(r-1, c)
                areaOfIsland(r, c+1)
                areaOfIsland(r, c-1)
                return self.currArea
        
        maxArea = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    maxArea = max(maxArea, areaOfIsland(r,c))
                    self.currArea = 0
        return maxArea
        
        