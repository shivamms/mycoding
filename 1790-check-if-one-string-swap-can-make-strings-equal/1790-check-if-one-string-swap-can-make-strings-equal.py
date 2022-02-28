class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        firstDiff = -1
        secondDiff = -1
        for i, x in enumerate(zip(s1, s2)):
            if x[0] != x[1]:
                if firstDiff < 0: 
                    firstDiff = i
                elif secondDiff < 0:
                    secondDiff = i
                elif firstDiff >= 0 and secondDiff >= 0:
                    return False
        if s1[firstDiff] == s2[secondDiff] and s2[firstDiff] == s1[secondDiff]:
                return True
        

            