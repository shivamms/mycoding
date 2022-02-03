class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        def compareStrings(set1, set2):
            for i in range(26):
                if set1[i] != set2[i]:
                    return False
            return True
        
        l = len(p)
        m = len(s)
        if l > m:
            return []
        set1 = [0]*26
        set2 = [0]*26
        result = []
        for i in range(l): set1[ord(p[i])-97] += 1
        for i in range(l): set2[ord(s[i])-97] += 1
        for i in range(l, m):
            if compareStrings(set1, set2):
                result.append(i-l)
            set2[ord(s[i-l])-97] -= 1
            set2[ord(s[i])-97] += 1
        if compareStrings(set1, set2):
                result.append(m-l)
        return result
        