class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        m = defaultdict(set)
        for (a, b), mult in zip(equations, values):
            m[a].add((b, mult))
            m[b].add((a, 1/mult))
        
        SCCs = {}
        memo = {}

        def dfs(v, scc):
            SCCs[v] = scc
            for u, w in m[v]:
                if u in SCCs:
                    continue
                memo[u] = memo[v] * w
                dfs(u, scc)
        
        cc = 0
        for s in m.keys():
            if s not in SCCs:
                cc += 1
                memo[s] = 1
                dfs(s, cc)

        def proc(s, f):
            if s not in SCCs or f not in SCCs:
                return -1
            if SCCs[s] != SCCs[f]:
                return -1
            return memo[f] / memo[s]
        
        return [proc(s, f) for (s, f) in queries]
