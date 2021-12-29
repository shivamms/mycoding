class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        queue = deque()
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '*':
                    queue.append((i,j,0))

        while queue:
            i, j, steps = queue.popleft()
            if 0<=i<rows and 0<=j<cols and grid[i][j] != 'X':
                if grid[i][j] == '#':
                    return steps
                grid[i][j] = 'X'
                for row, col in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                    queue.append((row, col, steps+1))
        return -1
        