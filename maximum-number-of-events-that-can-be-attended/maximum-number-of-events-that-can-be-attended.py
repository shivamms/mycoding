import heapq as hq
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        startEndMap = defaultdict(list)
        start, end = 10 ** 6, 0
        for s, e in events:
            if s < start:
                start = s
            if e > end:
                end = e
            startEndMap[s].append(e)

        count = 0
        available = []

        for d in range(start, end+1):
            if d in startEndMap:
                for e in startEndMap[d]:
                    hq.heappush(available, e)
            while available and available[0] < d:
                hq.heappop(available)
            if available and available[0] >= d:
                hq.heappop(available)
                count += 1
        return count

        