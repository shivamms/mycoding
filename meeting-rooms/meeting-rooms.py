class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals = sorted(intervals)
        if len(intervals) == 1:
            return True
        i = 0
        while i < len(intervals)-1:
            if intervals[i][1] > intervals[i+1][0]:
                return False
            i += 1
        return True