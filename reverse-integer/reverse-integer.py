class Solution:
    def reverse(self, x: int) -> int:
        numstr = "".join(list(reversed(str(x))))
        print(numstr)
        length = len(numstr)
        sign = ""
        if numstr[length-1] == "-" or numstr[length-1] == "+":
            numstr = numstr[length-1] + numstr[0:length-1]
        if -2**31 <= int(numstr) <= 2**31 - 1:
            return int(numstr)
        else:
            return 0
        
        