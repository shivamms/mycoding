class Solution(object):    
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        longest = ''
        for i, c in enumerate(s):
            substr = expand(s,i,i)
            if len(longest) < len(substr):
                longest = substr

        for i, c in enumerate(s):
            substr = expand(s,i,i+1)
            if len(longest) < len(substr):
                longest = substr
        return longest

def expand(s,low,high):
    strlen = len(s)
    while(low >= 0 and high < strlen and s[low] == s[high]):
        low -= 1
        high += 1
    return s[low+1:high]
        