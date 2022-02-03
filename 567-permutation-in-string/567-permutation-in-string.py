class Solution:
    from collections import Counter, defaultdict
    def checkInclusion(self, s1: str, s2: str) -> bool:
        set1 = Counter(s1)
        l = len(s1)
        for i in range(len(s2)):
            if set1 == Counter(s2[i:i+l]):
                return True
        return False
