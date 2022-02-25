class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(r,c):
            if r < 0 or r > m-1 or c < 0 or c > n-1 or grid[r][c] == "0":
                return
            if (r,c) not in visited:
                visited.add((r,c))
                dfs(r+1,c)
                dfs(r-1,c)
                dfs(r, c+1)
                dfs(r, c-1)
        
        m,n = len(grid), len(grid[0])
        islands = 0
        visited = set()
        for r in range(m):
            for c in range(n):
                if (r,c) not in visited and grid[r][c] == "1":
                    dfs(r,c)
                    islands += 1
        return islands
        


        