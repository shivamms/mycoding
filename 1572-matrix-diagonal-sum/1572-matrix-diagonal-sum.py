class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
          ## Recursion
        n = len(mat) 
        def getSum(r,c, dsum, colDir):
            if r <= n-1 and 0 <= c:
                dsum = mat[r][c] + getSum(r+1, c+colDir, dsum, colDir)
            return dsum
        
        dsum1 = getSum(0,0,0, 1) 
        dsum2 = getSum(0,n-1, 0, -1) 
        return dsum1 + dsum2 if n % 2 == 0 else dsum1 + dsum2 - mat[n//2][n//2]
        # n, dsum = len(mat), 0
        # while r 
        #         dsum += mat[r][c]