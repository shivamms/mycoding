class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] != 0 or grid[n-1][n-1] != 0:
            return -1
        
        def bfs(queue):
            visited = set()
            while queue:
                (row, col, distance) = queue.popleft()
                if (row, col) == (n-1, n-1):
                    return distance
                for (r,c) in ((row+1, col), (row-1, col), (row, col+1), (row, col-1), (row+1, col+1), (row-1, col-1), (row+1, col-1), (row-1, col+1)):
                    if 0 <= r < n and 0 <= c < n and grid[r][c] == 0 and (r, c) not in visited:

                        visited.add((r, c))
                        queue.append((r,c, distance + 1))
            return -1
                
                
        queue = deque()
        queue.append((0,0,1))
        return bfs(queue)