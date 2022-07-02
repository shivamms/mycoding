class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        end_time = []
        heapq.heappush(end_time, intervals[0][1])
        for m in intervals[1:]:
            if m[0] < end_time[0]:
                heapq.heappush(end_time, m[1])
            else:
                heapq.heapreplace(end_time, m[1])
        
        return(len(end_time))
            