class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        qs = queries.copy()
        qs.sort()
        intervals.sort(key=lambda x: x[0])
        h = []
        D = {}

        i = 0
        for q in qs:
            while i < len(intervals) and intervals[i][0] <= q:
                d = intervals[i][1] - intervals[i][0] + 1
                heapq.heappush(h, (d, intervals[i]))
                i += 1

            while h and h[0][1][1] < q:
                heapq.heappop(h)

            D[q] = h[0][0] if h else -1
        
        return [D[q] for q in queries]