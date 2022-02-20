class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = dict()
        longest = start = 0
        for end, c in enumerate(s):
            if c in seen:
                start = max(seen[c],start)
            longest = max(longest, end-start+1)
            seen[c] = end + 1
        return longest
                
        