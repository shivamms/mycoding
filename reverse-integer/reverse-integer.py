class Solution:
    def reverse(self, x: int) -> int:
        numstr = "".join(list(reversed(str(x))))
        length = len(numstr)
        if numstr[length-1] == "-" or numstr[length-1] == "+":
            numstr = numstr[length-1] + numstr[0:length-1]
        number = int(numstr)
        if -2**31 <= number <= 2**31 - 1:
            return number
        else:
            return 0
        
        