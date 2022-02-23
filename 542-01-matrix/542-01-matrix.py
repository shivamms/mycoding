class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        result = [[math.inf for j in range(n)] for i in range(m)]
        for r in range(m):
            for c in range(n):
                if mat[r][c] == 0:
                    result[r][c] = 0
                else:
                    if r > 0:
                        result[r][c] = min(result[r][c], result[r-1][c]+1)
                    if c > 0:
                        result[r][c] = min(result[r][c], result[r][c-1]+1)
        for r in range(m-1, -1, -1):
            for c in range(n-1, -1, -1):
                if r < m-1:
                    result[r][c] = min(result[r][c], result[r+1][c]+1)
                if c < n-1:
                    result[r][c] = min(result[r][c], result[r][c+1]+1)
        return result