class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowBuy = math.inf
        profit = curProfit = 0
        for p in prices:
            if p - lowBuy < curProfit:
                profit += curProfit
                curProfit = 0
                lowBuy = p
            else:
                curProfit = p-lowBuy
        return profit+curProfit
        