class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        ws = len(part)
        n = len(s)
        if n < ws:
            return s
        if s == part:
            return ""
        
        while part in s:
            string = s.replace(part, '',1)
            s = string
        return s
        