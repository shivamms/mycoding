class Solution:
    def merge(self,intervals: List[List[int]]) -> List[List[int]]:
        result = []
        intervals = sorted(intervals)
        while len(intervals) > 1:
            if intervals[0][0] <= intervals[1][0] <= intervals[0][1]:
                left = min(intervals[0][0],intervals[0][1],intervals[1][0],intervals[1][1])
                right = max(intervals[0][0],intervals[0][1],intervals[1][0],intervals[1][1])
                intervals[1][0] = left
                intervals[1][1] = right
            else:
                result.append(intervals[0])
            intervals = intervals[1:]
        result.append(intervals[0])
        return result

# intervals = [[1,3],[2,6],[8,10],[15,18]]
# intervals = [[1,4],[4,5]]
# intervals = [[1,4],[0,1]]
# intervals = [[1,4],[2,3]]
# print(merge(intervals))