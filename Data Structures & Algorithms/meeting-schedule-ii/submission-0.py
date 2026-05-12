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
        ends = []
        def room_ind(s):
            for i, end in enumerate(ends):
                if end <= s:
                    return i
            ends.append(s)
            return len(ends) - 1

        for interval in intervals:
            ind = room_ind(interval.start)
            ends[ind] = interval.end
        
        return len(ends)