class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        E = [[] for _ in range(n)]
        for u, v, price in flights:
            E[u].append((v, price))

        costs = [float("inf")] * n
        costs[src] = 0
        for _ in range(k + 1): # OFF BY ONE
            new_costs = costs.copy() # USE NEW COSTS TO AVOID CHAINING.
            for u in range(n):
                if costs[u] == float("inf"):
                    continue
                for v, price in E[u]:
                    new_costs[v] = min(new_costs[v], costs[u] + price)
            costs = new_costs

        if costs[dst] == float("inf"):
            return -1
        return costs[dst]