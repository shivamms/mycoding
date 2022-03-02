class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ## straightforward method taking advantage of sorted nature
        # m,n,row = len(matrix), len(matrix[0]), -1
        # for i in range(m):
        #     if target == matrix[i][n-1]: return True
        #     elif target < matrix[i][n-1]:
        #         row = i
        #         break
        # if target == matrix[row][0]: return True
        # else:
        #     for j in range(n):
        #         if target == matrix[row][j]: return True
        # return False
        
        ## binary search
        m,n,row = len(matrix), len(matrix[0]), -1
        left, right = 0, m*n-1
        while left <= right:
            mid = (left+right) // 2
            midVal = matrix[mid//n][mid%n]
            if target == midVal:
                return True
            else: 
                if target < midVal: 
                    right = mid - 1
                else: 
                    left = mid + 1
        return False