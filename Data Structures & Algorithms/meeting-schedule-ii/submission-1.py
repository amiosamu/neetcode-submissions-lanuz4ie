"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
from heapq import heappush, heappop


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        h = []
        intervals.sort(key=lambda x: x.start)

        heappush(h, intervals[0].end)

        for i in range(1, len(intervals)):
            current = intervals[i]
            if current.start >= h[0]:
                heappop(h)
            heappush(h, current.end)

        return len(h)