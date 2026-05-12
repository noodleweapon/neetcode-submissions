class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        buses = defaultdict(list) # buses at each stop
        n = len(routes) # num bus
        g = [[] for _ in range(n)]

        for i, stops in enumerate(routes):
            for stop in stops:
                for j in buses[stop]:
                    g[j].append(i)
                    g[i].append(j)
                buses[stop].append(i)
        
        dist = [float("inf")] * n
        h = []
        for i in buses[source]:
            dist[i] = 1
            h.append((i, 1))

        while h:
            i, d = heapq.heappop(h)
            if d > dist[i]:
                continue
            dist[i] = d
            for j in g[i]:
                if d + 1 < dist[j]:
                    heapq.heappush(h, (j, d + 1))

        M = float("inf")
        for i in buses[target]:
            M = min(M, dist[i])
        return M if M != float("inf") else -1
