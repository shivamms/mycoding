class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # m, n = len(mat), len(mat[0])
        # distance = [[math.inf for c in range(n)] for r in range(m)]
        # for r in range(m):
        #     for c in range(n):
        #         if mat[r][c] == 0:
        #             distance[r][c] = 0
        #         else:
        #             for (row, col) in ((r-1,c), (r, c-1)):
        #                 if 0 <= row < m and 0 <= col < n:
        #                     distance[r][c] = min(distance[row][col]+1, distance[r][c])
        # for r in range(m-1, -1 ,-1):
        #     for c in range(n-1, -1, -1):
        #         if mat[r][c] == 0:
        #             distance[r][c] = 0
        #         else:
        #             for (row, col) in ((r+1,c), (r, c+1)):
        #                 if 0 <= row < m and 0 <= col < n:
        #                     distance[r][c] = min(distance[row][col]+1, distance[r][c])
        # return distance

        # BFS
        m, n = len(mat), len(mat[0])
        distance = [[math.inf for c in range(n)] for r in range(m)]
        queue = deque()
        for r in range(m):
            for c in range(n):
                if mat[r][c] == 0:
                    distance[r][c] = 0
                    queue.append((r,c))

        while queue:
            (row, col) = queue.popleft()
            for (r, c) in ((row+1, col), (row-1,col), (row, col+1), (row, col-1)):
                if 0 <= r < m and 0 <= c < n and (r, c):
                    if distance[r][c] > distance[row][col]+1:
                        distance[r][c] = distance[row][col]+1
                        queue.append((r,c))
        return distance