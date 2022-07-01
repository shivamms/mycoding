class Solution:
    def compress(self, chars: List[str]) -> int:
        compstr, prev = '',''
        dupcount = 0
        for c in chars:
            if c != prev:
                if dupcount > 1:
                    compstr += str(dupcount)
                dupcount = 0
                compstr += c
            dupcount += 1
            prev = c
        if dupcount > 1:
            compstr += str(dupcount)
        for i, c in enumerate(compstr):
            chars[i] = c
        complen = len(compstr)
        chars = chars[:complen+1]
        return complen
        