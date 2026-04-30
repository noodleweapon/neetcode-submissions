"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) == 0:
            return True
        intervals.sort(key=lambda x: x[0])
        for i in range(len(intervals) - 1):
            a, b = intervals[i], intervals[i + 1]
            if a[1] > b[0]:
                return False
        return False