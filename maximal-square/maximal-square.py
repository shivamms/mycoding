class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        def checkSquare(i1,j1,i2,j2,area):
            size = ((i2-i1)+1) * ((j2-j1)+1)
            sqval = area + sum([int(c) for c in matrix[i2][j1:j2+1]])
            sqval +=  sum([int(r[j2]) for r in matrix[i1:i2]])
            if sqval < size:
                return area
            if size == sqval:
                area = max(size, area)
                if i2 + 1 < len(matrix) and j2+1 < len(matrix[0]):
                    return checkSquare(i1,j1,i2+1, j2+1,area)
            return area

        maxArea = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                area = checkSquare(i,j,i,j,0)
                maxArea = max(0 if area is None else area,maxArea)
        return maxArea
        