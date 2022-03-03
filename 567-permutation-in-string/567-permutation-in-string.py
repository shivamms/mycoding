class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        count1 = Counter(s1)
        for i in range(n-m+1):
            if count1 == Counter(s2[i:i+m]):
                return True
        return False
        