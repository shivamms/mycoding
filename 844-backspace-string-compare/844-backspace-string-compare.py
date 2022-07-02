class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        x,y='',''
        bs_count = 0
        for c in s[::-1]:
            if c == '#':
                bs_count += 1
            elif bs_count > 0:
                bs_count -= 1
            else:
                x += c
        bs_count = 0
        for c in t[::-1]:
            if c == '#':
                bs_count += 1
            elif bs_count > 0:
                bs_count -= 1
            else:
                y += c
        return x == y
            