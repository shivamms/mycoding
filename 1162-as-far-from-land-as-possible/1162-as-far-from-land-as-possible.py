class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        grid = [[0 if col else -1 for col in row] for row in grid]
        lands = deque([(r,c) for r in range(n) for c in range(n) if grid[r][c]==0])
        found = False
        while lands:
            land = lands.popleft()
            r, c = land[0], land[1]
            for (row, col) in ((r+1, c), (r-1,c), (r, c+1), (r, c-1)):
                if 0 <= row < n and 0 <= col < n and grid[row][col] == -1:
                    grid[row][col] = grid[r][c] + 1
                    lands.append((row,col))
                    found = True
        return max(itertools.chain.from_iterable(grid)) if found else -1
                    
                