class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        smallest = -1
        smallestDist = math.inf
        for i, p in enumerate(points):
            if x == p[0] or y == p[1]:
                dist = abs(x-p[0]) + abs(y-p[1])
                if dist < smallestDist:
                    smallestDist = dist 
                    smallest = i
        return smallest
                    
        