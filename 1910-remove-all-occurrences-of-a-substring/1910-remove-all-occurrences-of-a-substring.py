class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:        
        while part in s:
            string = s.replace(part, '',1)
            s = string
        return s
        