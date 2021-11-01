class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        groups, previous, start, end = [], s[0], 0, -1
        for i, c in enumerate(s):
            if c != previous:
                groups.append((start, end))
                start = i
                end = i
                previous = c
            else:
                end += 1
        groups.append((start, len(s)-1))

        binStrCount = 0
        for i in range(len(groups)-1):
            binStrCount += min(groups[i][1]-groups[i][0]+1,groups[i+1][1]-groups[i+1][0]+1)
        return binStrCount
        