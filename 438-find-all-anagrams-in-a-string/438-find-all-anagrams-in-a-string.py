class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:        
        l, m = len(p), len(s)
        if l > m: return []
        set1, set2 = [0]*26, [0]*26
        result = []
        for i in range(l): set1[ord(p[i])-97] += 1
        for i in range(l): set2[ord(s[i])-97] += 1
        for i in range(l, m):
            if set1 == set2:
                result.append(i-l)
            set2[ord(s[i-l])-97] -= 1
            set2[ord(s[i])-97] += 1
        if set1 == set2:
                result.append(m-l)
        return result
            
            
            
        