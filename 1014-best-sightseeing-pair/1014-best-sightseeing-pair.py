class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        maxVal = maxScore = 0
        dist = -1
        for num in values:
            dist += 1
            maxScore = max(maxScore, maxVal+num)
            if num >= maxVal:
                maxVal = num
                dist = 0
            maxVal -= 1
        return maxScore
        