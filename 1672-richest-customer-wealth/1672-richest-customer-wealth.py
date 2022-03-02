class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxWealth = 0
        for i in range(len(accounts)):
            maxWealth = max(maxWealth, sum(accounts[i]))
        return maxWealth