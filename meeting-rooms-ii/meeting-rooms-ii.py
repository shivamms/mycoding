class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # confRooms = 1
        # intervals.sort(key=lambda x: x[0])
        # roomsLatestEnd = []
        # heapq.heappush(roomsLatestEnd,intervals[0][1])
        # for i in range(1,len(intervals)):
        #     if roomsLatestEnd[0] > intervals[i][0]:
        #         confRooms += 1
        #     else:
        #         heapq.heappop(roomsLatestEnd)
        #     heapq.heappush(roomsLatestEnd,intervals[i][1])
        # return confRooms
        starts = sorted([i[0] for i in intervals])
        ends = sorted([i[1] for i in intervals])
        start = 0
        end = 0
        confRooms = 0
        while start < len(starts):
            if starts[start] < ends[end]:
                confRooms += 1
            else:
                end += 1
            start += 1
        return confRooms