class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        points = set(map(tuple, points))
        heap = [(0, next(iter(points)))]
        cost = 0
        while heap:
            d, u = heapq.heappop(heap)
            if u not in points:
                continue
            points.remove(u)
            cost += d

            for v in points:
                d2 = abs(u[0] - v[0]) + abs(u[1] - v[1])
                heapq.heappush(heap, (d2, v))
        return cost