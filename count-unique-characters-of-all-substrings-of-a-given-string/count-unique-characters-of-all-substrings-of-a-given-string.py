class Solution:
    def uniqueLetterString(self, s: str) -> int:
        # map for holding the position of each letter in the string
        alphaMap, n = defaultdict(lambda:-1), len(s)
        strFwdMap, strRevMap, result = [-1] * n, [-1] * n, 0
        for i, c in enumerate(s):
            if alphaMap[c] != -1: strFwdMap[alphaMap[c]] = i
            alphaMap[c] = i
        alphaMap = defaultdict(lambda:-1)
        for i in range(n-1, -1, -1):
            if alphaMap[s[i]] != -1: strRevMap[alphaMap[s[i]]] = i
            alphaMap[s[i]] = i
        # result += (i + 1) * (n - i) logic for non-dulicate
        for i in range(n):
            fwdAdj = n - 1 if strFwdMap[i] == -1 else strFwdMap[i] - 1
            revAdj = 0 if strRevMap[i] == -1 else strRevMap[i] + 1
            result += (i - revAdj + 1) * (fwdAdj - i + 1)
        return result
        
        
                