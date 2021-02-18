class Solution:
    def addStrings( self,num1: str, num2: str) -> str:
        carry = 0
        result = ""
        length1 = len(num1)
        length2 = len(num2)
        maxlen = max(length1,length2)
        minlen = min(length1,length2)
        num1 = num1[::-1]
        num2 = num2[::-1]
        for i in range(maxlen):
            if i < minlen:
                stepval =  carry + int(num1[i]) + int(num2[i])
            elif length1 == minlen:
                stepval =  carry + int(num2[i])
            elif length2 == minlen:
                stepval =  carry + int(num1[i])
            rem = stepval - 10
            if rem < 0:
                carry = 0
                result = str(stepval) + result
            else:
                carry = 1
                result = str(rem) + result
        if carry == 1:
            result = "1"+result
        return result