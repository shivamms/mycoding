class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashmap = {}
        start = 0
        maxlength = 0
        for i, ltr in enumerate(s):
            if ltr in hashmap:
                index = hashmap[ltr] + 1
                if index > start:
                    start = index
            length = (i - start) + 1
            if length > maxlength:
                maxlength = length
            hashmap[ltr] = i

        return maxlength
        