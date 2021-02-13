class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x >= 0:
            if x < 10:
                return True
            numstr = str(x)
            length = len(numstr)
            mid = int(length / 2)
            for i in range(mid):
                if numstr[i] != numstr[length - i - 1]:
                    return False
            return True
        return False