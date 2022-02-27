class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        dp = dict()
        closedIslands = 0
        def findIsland(r,c):
            if r < 0 or r > m-1 or c < 0 or c > n-1 or grid[r][c]==0:
                return
            # if grid[r][c] == 1:
            grid[r][c] = 0
            if r+1 <= m-1 and r-1 >= 0 and c+1 <= n-1 and c-1 >= 0:
                dp[(r,c)] = True
            else:
                dp[(r,c)] = False
            findIsland(r+1, c)
            findIsland(r-1, c)
            findIsland(r, c+1)
            findIsland(r, c-1)
            
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    findIsland(r,c)
                    if all(dp.values()):
                        closedIslands += len(dp)
                    dp = dict()
        return closedIslands