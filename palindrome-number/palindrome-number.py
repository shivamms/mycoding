class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x >= 0:
            if x < 10:
                return True
            numstr = str(x)
            length = len(numstr)
            for i in range(length):
                if numstr[i] != numstr[length - i - 1]:
                    return False
            return True
        return False
        