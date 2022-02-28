class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        heapq.heapify(arr)
        prev = heapq.heappop(arr)
        curr = heapq.heappop(arr)
        diff = curr-prev
        prev = curr
        while arr:
            curr = heapq.heappop(arr)
            if curr-prev != diff:
                return False
            prev = curr
        return True