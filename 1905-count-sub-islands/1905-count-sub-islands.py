class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def findIsland(grid,r,c,m,n,cells):
            if r < 0 or r > m-1 or c < 0 or c > n-1 or grid[r][c]==0:
                return
            grid[r][c] = 0
            cells.add((r,c))
            findIsland(grid,r+1, c,m,n,cells)
            findIsland(grid,r-1, c,m,n,cells)
            findIsland(grid,r, c+1,m,n,cells)
            findIsland(grid,r, c-1,m,n,cells)
        
        def collectIslands(grid):
            islands = []
            cells = set()
            m,n = len(grid), len(grid[0])
            for r in range(m):
                for c in range(n):
                    if grid[r][c] == 1:
                        findIsland(grid,r,c,m,n,cells)
                        islands.append(cells)
                        cells = set()
            return islands
        
        # islands1 = collectIslands(grid1)
        islands2 = collectIslands(grid2)
        subIslands = 0
        for land in islands2:
            subIsland = True
            for cell in land:
                if grid1[cell[0]][cell[1]] == 0:
                    subIsland = False
                    break
            if subIsland:
                subIslands += 1
        return subIslands
                    