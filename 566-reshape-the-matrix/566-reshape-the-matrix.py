class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        if r*c != m*n:
            return mat
        reshaped = [[0 for j in range(c)] for i in range(r)]
        x = y = 0
        for i in range(m):
            for j in range(n):
                reshaped[x][y] = mat[i][j]
                y += 1
                if y > c-1:
                    y = 0
                    x += 1
        return reshaped
                
        
        