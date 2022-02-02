class Solution:
    from collections import defaultdict
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        n = len(words)
        alpha = defaultdict(int)
        i = 1
        for c in order:
            alpha[c] = i
            i += 1
        for i in range(n-1):
            word1 = words[i]
            word2 = words[i+1]
            l, m = len(word1), len(word2)
            j = 0
            while j < min(l,m):
                if alpha[word1[j]] < alpha[word2[j]]:
                    break
                elif alpha[word1[j]] == alpha[word2[j]]:
                    j += 1
                else:
                    return False
            if l > m and j == m:
                return False
        return True
                
        