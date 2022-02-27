class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        # numStr = str(n)
        # digitSum, digitProd = 0, 1
        # for d in numStr:
        #     digitNum = int(d)
        #     digitSum += digitNum
        #     digitProd *= digitNum
        # return digitProd - digitSum
        digitSum, digitProd = 0, 1
        while n > 0:
            digit = n % 10
            digitSum += digit
            digitProd *= digit
            n = n //10
        return digitProd - digitSum
        
        