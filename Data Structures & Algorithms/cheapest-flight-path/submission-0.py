class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        h = [(0, src, 0)]
        E = defaultdict(list)
        for (from_i, to_i, price_i) in flights:
            E[from_i].append((to_i, price_i))
        
        visited = [False] * n
        while h:
            (d, v, stops) = heapq.heappop(h)
            if visited[v]:
                continue
            if stops > k + 1:
                continue
            visited[v] = True
            if v == dst:
                return d
            
            for (u, price) in E[v]:
                if visited[u]:
                    continue
                heapq.heappush(h, (d + price, u, stops + 1))
        return -1