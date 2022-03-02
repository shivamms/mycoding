class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n,row = len(matrix), len(matrix[0]), -1
        for i in range(m):
            if target == matrix[i][n-1]: return True
            elif target < matrix[i][n-1]:
                row = i
                break
        if target == matrix[row][0]: return True
        else:
            for j in range(n):
                if target == matrix[row][j]: return True
        return False