class Solution:

    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        magicsquarecount = 0
        square = []
        rowlength = len(grid)
        squaredic = {}
        validsqure = True
        if rowlength >= 3:
            for i in range(rowlength - 2):
                collength = len(grid[i])
                rows = grid[i:i+3]
                if collength >= 3:
                    for j in range(collength-2):
                        for r, row in enumerate(rows):
                            for n in row[j:j+3]:
                                if n in squaredic.keys() or n > 9 or n <= 0:
                                    validsqure = False
                                    break
                                squaredic[n] = True   
                            if validsqure:
                                square.append(row[j:j+3])
                        squaredic = {}
                        if validsqure and self.isMagicSquare(square):
                            magicsquarecount += 1
                        square = []
                        validsqure = True
        return magicsquarecount


    def isMagicSquare(self,square: List[List[int]]) -> bool:
        return all([square[0][0] +  square[0][1] + square[0][2] == square[0][0] +  square[1][0] + square[2][0],
                        square[0][0] +  square[1][0] + square[2][0] == square[1][0] +  square[1][1] + square[1][2],
                        square[1][0] +  square[1][1] + square[1][2] == square[0][1] +  square[1][1] + square[2][1],
                        square[0][1] +  square[1][1] + square[2][1] == square[2][0] +  square[2][1] + square[2][2],
                        square[2][0] +  square[2][1] + square[2][2] == square[0][2] +  square[1][2] + square[2][2],
                        square[0][2] +  square[1][2] + square[2][2] == square[0][0] +  square[1][1] + square[2][2],
                        square[0][0] +  square[1][1] + square[2][2] == square[0][2] +  square[1][1] + square[2][0]])
            
            
        