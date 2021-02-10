class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = len(s)
        if n == 1 or numRows == 1:
            return s
        interval = (2*numRows) - 2
        convstr = ""
        for i in range(numRows):
            for c in range(i,n,interval):
                convstr = convstr + s[c]
                if numRows-1 > i > 0 and c+interval-2*i < n:
                    convstr = convstr + s[c+interval-2*i]
        return convstr