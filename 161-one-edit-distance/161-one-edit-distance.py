class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        m,n = len(s), len(t)
        if abs(m-n) > 1 or (not m and not n):
            return False
        i,j = 0, 0
        diffSeen = 0
        while i < m and j < n:
            if s[i] != t[j]:
                if diffSeen > 0:
                    return False
                else:
                    diffSeen += 1
                    if m > n:
                        i += 1
                    elif m < n:
                        j += 1
                    else:
                        i += 1
                        j += 1
            else:
                i += 1
                j += 1
        if diffSeen == 0 and (m-i == 1 or n-j == 1):
            diffSeen += 1
        return True if diffSeen == 1 else False
        
        
                        
        
        