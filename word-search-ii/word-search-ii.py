class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        _end = '_end'
        rows, cols = len(board), len(board[0])
        def makeTrie():
            root = dict()
            for word in words:
                curr = root
                for letter in word:
                    curr = curr.setdefault(letter, {})
                curr.setdefault(_end, _end)
            return root

        wordTrie = makeTrie()
        foundWords = []

        def checkWords(i,j,node,prefix): 
            letter = board[i][j] 
            if letter in node: 
                board[i][j] = '#'
                prefix += letter 
                node = node[letter] 
                if _end in node:
                    foundWords.append(prefix)
                    del node[_end]
                for r, c in (i+1, j), (i-1, j), (i, j+1), (i, j-1): 
                    if 0 <= r < rows and 0 <= c < cols:
                        checkWords(r,c,node,prefix) 
                board[i][j] = letter

        for i in range(len(board)):
            for j in range(len(board[0])): 
                prefix = ''
                checkWords(i,j,wordTrie,prefix) 

        return(foundWords)