class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        i, j = 0, n-1
        while i <= j:
            left, right = ord(s[i].lower()), ord(s[j].lower())
            if not 97 <= left <= 122 and not 48 <= left <= 57:
                i += 1
            if not 97 <= right <= 122 and not 48 <= right <= 57:
                j -= 1
            if (97 <= left <= 122 or 48 <= left <= 57) and (97 <= right <= 122 or 48 <= right <= 57):
                if left != right:
                    return False
                else:
                    i += 1
                    j -= 1
        return True