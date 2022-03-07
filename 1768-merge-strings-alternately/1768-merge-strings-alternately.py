class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ''
        m,n, i = len(word1), len(word2), 0
        while i < m and i < n:
            merged += word1[i] + word2[i]
            i += 1
        merged += word1[i:] + word2[i:]
        return merged