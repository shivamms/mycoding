class Solution:
    from collections import defaultdict
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        numberCounts = defaultdict(int)
        pq = []
        for n in arr:
            numberCounts[n] += 1
        for key, value in numberCounts.items():
            heappush(pq, (value, key))
        while k > 0:
            if k - pq[0][0] >= 0:
                k -= heappop(pq)[0]      
            else:
                k = 0
        return len(pq)

            
            