class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seenSet, longest, start = dict(), 0, 0
        for i, c in enumerate(s):
            if c in seenSet:               
                start = max(seenSet[c], start)
            longest = max(longest, i - start + 1)
            seenSet[c] = i + 1
        return longest