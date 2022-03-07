class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        orderMap = dict()
        for i, l in enumerate(order):
            orderMap[l] = i
        prev = words[0]
        for curr in words[1:]:
            m,n, i = len(prev), len(curr), 0
            while m > i < n:
                if orderMap[prev[i]] < orderMap[curr[i]]:
                    break
                elif orderMap[prev[i]] > orderMap[curr[i]]:
                    return False
                i += 1
            prev = curr
            if i < m and i == n:
                return False
        return True
        