class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
            
        def bfs(queue):        
            edgeSet = set()
            while queue:
                (row, col) = queue.popleft()
                edgeSet.add((row, col))
                for (r, c) in ((row+1, col), (row-1, col), (row, col+1), (row, col-1)):
                    if 0 <= r < m and 0 <= c < n and (r,c) not in edgeSet and heights[r][c] >= heights[row][col]:
                        queue.append((r, c))
            return edgeSet
                        
            
        queue = deque()
        for r in range(m):
            queue.append((r, 0))
        for c in range(1,n):
            queue.append((0, c))
        pacificSet = bfs(queue)
        queue = deque() 
        for r in range(m):
            queue.append((r, n-1))
        for c in range(n-1):
            queue.append((m-1, c))
        atlanticSet = bfs(queue)
        
        return pacificSet.intersection(atlanticSet)
                
                
                