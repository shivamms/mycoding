class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pTriangle = [[1]]
        level = 2
        levelArr = []
        while level <= numRows:
            prevRow = pTriangle[-1]
            for i in range(level):
                if i == 0 or i == level-1:
                    levelArr.append(1)
                else:
                    levelArr.append(prevRow[i-1]+prevRow[i])
            pTriangle.append(levelArr)
            levelArr = []
            level += 1
        return pTriangle