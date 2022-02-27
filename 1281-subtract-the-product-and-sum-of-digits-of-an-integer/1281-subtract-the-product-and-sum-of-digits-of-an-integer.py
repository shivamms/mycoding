class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        numStr = str(n)
        digitSum, digitProd = 0, 1
        for d in numStr:
            digitNum = int(d)
            digitSum += digitNum
            digitProd *= digitNum
        return digitProd - digitSum
        
        