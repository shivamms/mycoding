class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(i,j):
            return all(s[k] == s[j - k + i] for k in range(i,j))

        for i in range(len(s)//2):
            if s[i] != s[~i]:
                j = len(s) + (~i)
                return isPalindrome(i+1, j) or isPalindrome(i, j-1)
        return True
