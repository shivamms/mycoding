class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowBuy = math.inf
        profit = 0
        for p in prices:
            profit = max(profit, p-lowBuy)
            lowBuy = min(lowBuy, p)
        return profit
                