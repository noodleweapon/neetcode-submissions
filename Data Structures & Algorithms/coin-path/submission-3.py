class Solution:
    def cheapestJump(self, coins: List[int], maxJump: int) -> List[int]:
        n = len(coins)
        cost = [float("inf")] * n
        E = [set() for _ in range(n)]
        cost[0] = 0
        for i in range(n):
            if cost[i] == float("inf"):
                continue # MISTAKE: I put return [] here
            for j in range(i + 1, min(n, i + maxJump + 1)):
                if coins[j] == -1:
                    continue
                new_cost = cost[i] + coins[j]
                if new_cost <= cost[j]:
                    cost[j] = new_cost
                    E[i].add(j)

        if cost[-1] == float("inf"):
            return []

        res = []
        def dfs(u):
            if u == n - 1:
                return [n - 1]
            for v in E[u]:
                tail = dfs(v)
                if tail != None:
                    return [u] + tail

            return None
        
        res = dfs(0)
        return list(map(lambda x : x + 1, res))
