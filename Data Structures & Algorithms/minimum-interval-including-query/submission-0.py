class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        res = []
        for q in queries:
            h = []
            for interval in intervals:
                d = interval[1] - interval[0] + 1
                if interval[0] <= q <= interval[1]:
                    heapq.heappush(h, (d, interval))
            if h:
                res.append(heapq.heappop(h)[0])
            else:
                res.append(-1)
        return res