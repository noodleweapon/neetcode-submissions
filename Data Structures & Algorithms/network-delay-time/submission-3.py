class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        d = defaultdict(list)
        for u, v, t in times:
            d[u].append((v, t))
        visited = [False] * (n + 1)
        total_visits = 0
        
        h = [(0, k)]
        while h:
            accum_t, u = heapq.heappop(h)
            if visited[u]:
                continue
            visited[u] = True
            total_visits += 1
            if total_visits == n:
                return accum_t
            for v, edge_t in d[u]:
                if not visited[v]:
                    heapq.heappush(h, (accum_t + edge_t, v))
        return -1
        