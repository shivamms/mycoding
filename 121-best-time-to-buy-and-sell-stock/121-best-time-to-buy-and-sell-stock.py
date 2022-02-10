class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = highest = prices[0]
        maxProfit = 0
        for p in prices:
            if p < lowest:
                lowest = highest = p
            elif p > highest:
                highest = p
            maxProfit = max(highest - lowest, maxProfit)
        return maxProfit
                