class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        cost = 0
        heapq.heapify(sticks)
        while sticks:
            stick1 = heapq.heappop(sticks)
            if sticks:
                stick2 = heapq.heappop(sticks)
            else:
                break
            connectedsticks = stick1 + stick2
            cost += connectedsticks
            heapq.heappush(sticks,connectedsticks)
        return cost