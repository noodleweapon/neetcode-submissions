class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x[0])
        end = intervals[0][1]
        n = 0
        for interval in intervals[1:]:
            if interval[0] < end:
                n += 1
                end = min(end, interval[1])
            else:
                end = interval[1]
        return n
