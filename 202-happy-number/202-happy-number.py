class Solution:
    def isHappy(self, n: int) -> bool:
        def digitSqrSum(num):
            digitSum = 0
            while num > 0:
                digitSum += (num % 10)**2
                num = num // 10
            return digitSum
        
        num = n
        i = 0
        while i < 10:
            num = digitSqrSum(num)
            if num == 1: return True
            if num == n: return False
            i += 1