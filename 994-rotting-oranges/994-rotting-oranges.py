class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        rotten = deque()
        fresh = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    rotten.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1
        rotten.append((-1,-1))
        minutes = -1
        while rotten:
            cell = rotten.popleft()
            if cell[0] == -1:
                minutes += 1
                if rotten:
                    rotten.append((-1,-1))
            else:
                for dist in [(1,0),(-1,0),(0,1),(0,-1)]:
                    row, col = cell[0]+dist[0], cell[1]+dist[1]
                    if 0 <= row < m and 0 <= col < n and grid[row][col] == 1:
                        grid[row][col] = 2
                        fresh -= 1
                        rotten.append((row, col))
        return minutes if fresh == 0 else -1
                
                    
                
        