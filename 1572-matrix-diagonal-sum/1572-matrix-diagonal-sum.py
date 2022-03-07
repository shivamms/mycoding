class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat) 
        def getSum(r,c, dsum, colDir):
            if 0 <= r <= n-1 and 0 <= c <= n-1:
                dsum = mat[r][c] + getSum(r+1, c+colDir, dsum, colDir)
            return dsum
        
        dsum1 = getSum(0,0,0, 1) 
        dsum2 = getSum(0,n-1, 0, -1) 
        return dsum1 + dsum2 if n % 2 == 0 else dsum1 + dsum2 - mat[n//2][n//2]