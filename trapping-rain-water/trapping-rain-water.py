import heapq as hq
class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        queue = []
        trappedWater = 0

        for h in height:
            if not queue or h >= (queue[0] * -1):
                hq.heappush(queue, h * -1)
                stack = []
            elif h < (queue[0] * -1):
                stack.append((queue[0] * -1) - h)
                trappedWater += stack[-1]

        prev = 1000000
        lastHeight = queue[0] * -1
        while stack:
            curr = stack.pop()
            if curr <= prev:
                trappedWater -= curr
            else:
                trappedWater -= prev
            prev = min(curr, prev)
        return trappedWater
        