class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ## hashmap
        # s,t = Counter(s), Counter(t)
        # if len(s) > len(t):
        #     for key, val in s.items():
        #         if val != t[key] or key not in t:
        #             return key
        # else:
        #     for key, val in t.items():
        #         if val != s[key] or key not in s:
        #             return key
                
        ## bit manipulation - XOR
        ch = 0
        for l in s: ch ^= ord(l)
        for l in t: ch ^= ord(l)
        return chr(ch)