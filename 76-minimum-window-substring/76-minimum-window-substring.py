class Solution:
    from collections import defaultdict, Counter
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        indexMap = Counter(t)
        fs = tuple((i, c) for i,c in enumerate(s) if c in indexMap)
        if not fs:
            return ""
        left, right, windowStart, windowEnd, windowSize = 0,0,0,0,inf
        windowMap = defaultdict(int) 
        charCountCovered, charCount = 0, len(indexMap)
        while right < len(fs):
            c = fs[right][1]
            windowMap[c] += 1
            if windowMap[c] == indexMap[c]:
                charCountCovered += 1
            while left <= right and charCount == charCountCovered:
                start, end = fs[left][0], fs[right][0]
                if windowSize > (end-start) + 1:
                    windowStart, windowEnd = start, end 
                    windowSize =  (end-start) + 1
                c = fs[left][1]
                windowMap[c] -= 1
                if windowMap[c] < indexMap[c]:
                    charCountCovered -= 1
                left += 1
            right += 1
        return "" if windowSize == inf else s[windowStart:windowEnd+1]
            
                