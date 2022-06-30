class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        n = len(stones)
        if n == 1:
            return stones[0]
        stones = [-stones[i] for i in range(n)]
        heapify(stones)
        while len(stones) > 1:
            y,x = heappop(stones), heappop(stones)
            if y != x:
                heappush(stones, y-x)
        return -stones[0] if stones else 0