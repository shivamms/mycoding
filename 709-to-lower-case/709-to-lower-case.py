class Solution:
    def toLowerCase(self, s: str) -> str:
        # return ''.join([chr(ord(l)+32) if 65 <= ord(l) <= 90 else l for l in s])
        return s.lower()