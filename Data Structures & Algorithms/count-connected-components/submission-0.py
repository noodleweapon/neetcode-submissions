class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        seen = [False] * n
        adj = [[] for _ in range(n)]
        for [a, b] in edges:
            adj[a].append(b)
            adj[b].append(a)

        def dfs(i):
            if seen[i]:
                return
            seen[i] = True
            for j in adj[i]:
                dfs(j)

        cc = 0
        for i in range(n):
            if seen[i]:
                continue
            dfs(i)
            cc += 1
        return cc