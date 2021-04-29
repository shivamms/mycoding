class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        orderHash = {c:i for i, c in enumerate(order)}
        for i in range(len(words)-1):
            j = 0
            while j < min(len(words[i]),len(words[i+1])):
                if orderHash[words[i][j]] < orderHash[words[i+1][j]]:
                    j += 1
                    break
                elif orderHash[words[i][j]] > orderHash[words[i+1][j]]:
                    return False
                j += 1
            if orderHash[words[i][j-1]] == orderHash[words[i+1][j-1]] and len(words[i]) > len(words[i+1]):
                return False
        return True