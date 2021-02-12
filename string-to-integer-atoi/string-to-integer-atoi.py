class Solution:
    def myAtoi(self, s: str) -> int:
        if len(s) == 0:
            return 0
        s = s.lstrip(" ")
        if len(s) > 0:
            sign = ""
            if s[0] == "-" or s[0] == "+":
                sign = s[0]
                s = s[1:]
            for i, c in enumerate(s):
                if ord(c) < 48 or ord(c) > 57:
                    s = s[:i]
                    break
            if len(s) == 0:
                return 0
            else:
                n = int(sign + s)
                if n < -2 ** 31:
                    return -2 ** 31
                elif n > 2 ** 31 - 1:
                    return 2 ** 31 - 1
            return n
        else:
            return 0
            
        