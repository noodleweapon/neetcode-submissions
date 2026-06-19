class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        d = collections.defaultdict(list)
        for u, v, price in flights:
            d[u].append((v, price))
        
        gas = [-1] * n
        h = [(0, src, k + 1)]
        while h:
            p, u, g = heapq.heappop(h)
            if u == dst:
                return p
            if g <= gas[u]:
                continue
            gas[u] = g
            if g - 1 >= 0:
                for v, edge_p in d[u]:
                    if g - 1 > gas[v]:
                        heapq.heappush(h, (p + edge_p, v, g - 1))
        
        return -1