import heapq
class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        inventory.sort()
        overlappedcount = 1
        profit = 0
        while orders > 0 and len(inventory) >= 2 and (inventory[-1] - inventory[-2]) * overlappedcount <= orders:
            col1, col2 = inventory[-1], inventory[-2]
            numOrders = (col1 - col2)
            col1OnlySales = ((col1 * (col1 + 1))//2) - ((col2 * (col2 + 1))//2)
            profit += col1OnlySales * overlappedcount
            orders -= numOrders * overlappedcount
            overlappedcount += 1
            inventory.pop()
        numOrders = (orders // overlappedcount)
        col1, col2 = inventory[-1], inventory[-1] - numOrders
        col1OnlySales = ((col1 * (col1 + 1)) // 2) - ((col2 * (col2 + 1)) // 2)

        profit += col1OnlySales * overlappedcount
        orders -= numOrders * overlappedcount

        profit += orders * col2

        return int(profit % 1000000007)