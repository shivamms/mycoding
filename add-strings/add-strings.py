class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        sum = 0
        length1 = len(num1)
        length2 = len(num2)
        maxlength = max(length1,length2)
        if maxlength == length1:
            prenum = num1[:length1-length2]
            diff = length1-length2
            length = length1
        else:
            prenum = num2[:length2-length1]
            diff = length2-length1
            length = length2
        for i,n in enumerate(prenum):
            sum += int(n) * 10 ** (length-i-1)
        for j in range(diff,length):
            if maxlength == length1:
                sum += int(num1[j]) * 10 ** (length-j-1) + int(num2[j-diff]) * 10 ** (length-j-1)
            else:
                sum += int(num2[j]) * 10 ** (length-j-1) + int(num1[j-diff]) * 10 ** (length-j-1)
        return str(sum)
            