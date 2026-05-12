"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)
        h = []
        for interval in intervals:
            if h and h[0] <= interval.start:
                heapq.heapreplace(h, interval.end)
            else:
                heapq.heappush(h, interval.end)
        return len(h)