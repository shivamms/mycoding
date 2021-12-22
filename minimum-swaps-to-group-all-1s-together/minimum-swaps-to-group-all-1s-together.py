class Solution:
    def minSwaps(self, data: List[int]) -> int:
        size = len(data) 
        swaps, minSwaps = 0, size
        ones = sum([1 for i in range(size) if data[i]==1])
        if ones <= 0:
            return 0
        onesCount = sum([1 for i in range(ones) if data[i]==1])

        windowStart = 0
        windowEnd = windowStart + ones - 1
        while windowEnd < size:
            swaps = ones - onesCount
            minSwaps = min(minSwaps, swaps)
            onesCount -= data[windowStart]
            windowStart += 1
            windowEnd += 1
            if windowEnd < size:
                onesCount += data[windowEnd]
            
        return minSwaps