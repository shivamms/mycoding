class Solution:
    import heapq
    from collections import defaultdict
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distHeap = []
        pointsDistHash = defaultdict(list)
        for p in points:
            dist = math.sqrt(p[0]**2 + p[1]**2)
            heapq.heappush(distHeap, dist)
            pointsDistHash[dist].append(p)
        res = []
        i = 0
        while i < k:
            for p in pointsDistHash[heapq.heappop(distHeap)]:
                res.append(p)        
                i += 1
        return res