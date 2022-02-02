class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        overlappedInt = []
        i, j = 0, 0
        n = len(firstList)
        m = len(secondList)
        while i < n and j < m:
            start = max(firstList[i][0], secondList[j][0])
            end = min(firstList[i][1], secondList[j][1])
            
            if start <= end:
                overlappedInt.append([start, end])
            
            if firstList[i][1] < secondList[j][1]:
                i += 1
            elif firstList[i][1] > secondList[j][1]:
                j += 1
            else:
                i += 1
                j += 1
        return overlappedInt
            
            
        