class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        shortest = [-1] * n
        h = [(0, k)]
        E = defaultdict(list)
        for (u, v, t) in times:
            E[u].append((v, t))

        while h:
            (d, u) = heapq.heappop(h)
            if shortest[u - 1] != -1:
                continue
            shortest[u - 1] = d
            for (v, t) in E[u]:
                if shortest[v - 1] == -1:
                    heapq.heappush(h, (t + d, v))

        if -1 in shortest:
            return -1
        return max(shortest)