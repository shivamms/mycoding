class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        ## BFS
        m,n = len(maze), len(maze[0])
        queue = deque()
        queue.append(entrance)
        queue.append(None)
        path = 1
        while queue:
            cell = queue.popleft()
            if cell:
                for (row, col) in ((cell[0]+1, cell[1]), (cell[0]-1, cell[1]), (cell[0], cell[1]+1),(cell[0], cell[1]-1)):
                    if 0 <= row < m and 0 <= col < n:
                        if (row == 0 or row == m-1 or col == 0 or col == n-1) and [row, col] != entrance and maze[row][col] == '.':
                            return path
                        elif maze[row][col] == '.':
                            maze[row][col] = '+'
                            queue.append((row, col))
            else:
                path += 1
                if queue:
                    queue.append(None)
        return -1