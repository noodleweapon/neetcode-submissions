class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        def dist(p1, p2):
            (x1, y1) = p1
            (x2, y2) = p2
            return abs(x1 - x2) + abs(y1 - y2)
        

        visited = [False] * N
        D = 0
        h = [(0, 0)]
        while h:
            (d, i) = heapq.heappop(h)
            if visited[i]:
                continue
            visited[i] = True
            D += d
            for j in range(N):
                if visited[j]:
                    continue
                dist_ij = dist(points[i], points[j])
                heapq.heappush(h, (dist_ij, j))

        return D