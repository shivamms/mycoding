import heapq
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes = sorted(boxTypes, key=lambda x: x[1], reverse=True)
        boxCount = 0
        maxUnits = 0
        for box in boxTypes:
            boxCount += box[0]
            if boxCount > truckSize:
                maxUnits +=  (truckSize - (boxCount - box[0])) * box[1]
                return maxUnits
            else:
                maxUnits += box[0] * box[1]
        
        return maxUnits