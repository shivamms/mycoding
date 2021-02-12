class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip(" ")
        if len(s) > 0:
            sign = ""
            if s[0] in ["-","+"]:
                sign = s[0]
                s = s[1:]
            for i, c in enumerate(s):
                val = ord(c)
                if val < 48 or val > 57:
                    s = s[:i]
                    break
            if len(s) > 0:
                n = int(sign + s)
                if n < -2 ** 31:
                    return -2 ** 31
                elif n > 2 ** 31 - 1:
                    return 2 ** 31 - 1
                return n
        return 0
            
        