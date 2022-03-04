class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        islands = []
        m,n = len(grid), len(grid[0])
        visited = set()
        def findIslands(r,c):
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == 0:
                return
            if (r,c) not in visited and grid[r][c] == 1:
                visited.add((r,c))
                island.add((r,c))
                for (row, col) in ((r+1, c), (r-1, c), (r, c+1), (r, c-1)): 
                    findIslands(row,col)
                return island
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    island = set()
                    findIslands(r,c)
                    if island:
                        islands.append(island)  
                        
        bridge = 0
        queue = deque()
        for cell in islands[0]:
            queue.append(cell)
        queue.append(None)
        while queue:
            land = queue.popleft()
            if land:
                r, c = land[0], land[1]
                for (row, col) in ((r+1, c), (r-1,c), (r, c+1), (r, c-1)):
                    if row < 0 or row >= m or col < 0 or col >= n or (row, col) in islands[0]:
                        continue
                    elif (row, col) in islands[1]:
                        return bridge
                    elif grid[row][col] == 0:
                        grid[row][col] += grid[r][c]   
                        queue.append((row, col))
            else:
                queue.append(None)
                bridge += 1
            

        
                
            
            
        