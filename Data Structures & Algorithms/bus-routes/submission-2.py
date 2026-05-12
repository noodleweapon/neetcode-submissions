class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        buses = defaultdict(list) # buses at each stop
        n = len(routes) # num bus
        arrived = [False] * n
        visited = [False] * n
        g = [[] for _ in range(n)]

        for i, stops in enumerate(routes):
            for stop in stops:
                if stop == target:
                    arrived[i] = True
                for j in buses[stop]:
                    g[j].append(i)
                    g[i].append(j)
                buses[stop].append(i)
        
        d = 0
        q = deque()
        for i in buses[source]:
            visited[i] = True
            q.append(i)

        while q:
            d += 1
            for _ in range(len(q)):
                i = q.popleft()
                if arrived[i]:
                    return d
                for j in g[i]:
                    if not visited[j]:
                        visited[j] = True
                        q.append(j)

        return -1
