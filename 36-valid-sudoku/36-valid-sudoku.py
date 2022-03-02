class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m, n = len(board), len(board[0])
        colSet = [set() for _ in range(n)]
        boxSet = [set() for _ in range(n)]
        for i in range(m):
            j = 0
            box = 0
            rowSet = set()
            for r in board[i]:
                if r in rowSet: return False
                if r != '.': rowSet.add(r)
                if board[i][j] in colSet[j]: return False
                if board[i][j] != '.': colSet[j].add(board[i][j])
                boxIndex = (i // 3) * 3 + (j // 3)
                if board[i][j] in boxSet[boxIndex]: return False
                if board[i][j] != '.': boxSet[boxIndex].add(board[i][j])
                j += 1

        return True
    

            