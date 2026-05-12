class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        def dist(p1, p2):
            (x1, y1) = p1
            (x2, y2) = p2
            return abs(x1 - x2) + abs(y1 - y2)
        
        visited = [False] * n
        h = [(0, 0)]
        cost = 0
        visits = 0
        while visits < n: # n rather than n-1 cause counting vertices.
            (d, u) = heapq.heappop(h)
            if visited[u]:
                continue
            visited[u] = True
            cost += d
            visits += 1
            for v, point in enumerate(points):
                if not visited[v]:
                    d2 = dist(points[u], points[v])
                    heapq.heappush(h, (d2, v))
        
        return cost