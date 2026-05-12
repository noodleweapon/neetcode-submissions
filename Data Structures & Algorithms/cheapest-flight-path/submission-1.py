class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        h = [(0, src, k + 1)]
        E = defaultdict(list)
        for (from_i, to_i, price_i) in flights:
            E[from_i].append((to_i, price_i))
        
        visited = [-1] * n

        while h:
            (d, v, gas) = heapq.heappop(h)
            if visited[v] >= gas:
                continue
            if gas < 0:
                continue
            visited[v] = gas
            if v == dst:
                return d
            
            for (u, price) in E[v]:
                heapq.heappush(h, (d + price, u, gas - 1))
        return -1