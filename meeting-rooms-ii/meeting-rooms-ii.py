class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        confRooms = 1
        intervals.sort(key=lambda x: x[0])
        end = intervals[0][1]
        roomsLatestEnd = []
        heapq.heappush(roomsLatestEnd,intervals[0][1])
        for i in range(1,len(intervals)):
            if end > intervals[i][0]:
                confRooms += 1
                heapq.heappush(roomsLatestEnd,intervals[i][1])
            else:
                heapq.heappop(roomsLatestEnd)
                heapq.heappush(roomsLatestEnd,intervals[i][1])
            end = min(roomsLatestEnd)
        return confRooms
        
        