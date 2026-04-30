class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        H = [(0, k)]
        E = [[] for _ in range(n + 1)]
        for (u, v, t) in times:
            E[u].append((v, t))
        dist = []
        for i in range(n + 1):
            dist.append(0 if i == k else float("inf"))
        
        while H:
            (d, u) = heapq.heappop(H)
            for (v, t) in E[u]:
                new_dist = dist[u] + t
                if dist[v] <= new_dist:
                    dist[v] = new_dist
                    heapq.heappush(H, (new_dist, v))
        
        M = max(dist)
        if M == float("inf"):
            return -1
        return M