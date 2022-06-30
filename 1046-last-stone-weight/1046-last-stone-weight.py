class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        n = len(stones)
        if n == 1:
            return stones[0]
        stones = [-stones[i] for i in range(n)]
        heapify(stones)
        while len(stones) > 1:
            y,x = heappop(stones), heappop(stones)
            if abs(y)-abs(x) > 0:
                heappush(stones,-(abs(y)-abs(x)))
        return -stones[0] if len(stones) == 1 else 0