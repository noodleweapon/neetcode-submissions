class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        d = defaultdict(list)
        n = len(tickets)
        for u, v in tickets:
            d[u].append(v)
        used = {}
        for u in d:
            d[u].sort()
            used[u] = [False] * len(d[u])
        
        res = ["JFK"]
        def dfs(u, used_count):
            if used_count == n:
                return True
            for i, v in enumerate(d[u]):
                if used[u][i]:
                    continue
                used[u][i] = True
                res.append(v)
                if dfs(v, used_count + 1):
                    return True
                res.pop()
                used[u][i] = False
            return False
        
        dfs("JFK", 0)
        return res
        