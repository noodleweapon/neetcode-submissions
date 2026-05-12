class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = [[] for _ in range(n)]
        v = [0] * n
        for [a, b] in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        def dfs(i, parent):
            if v[i] == 2:
                return False # visited
            if v[i] == 1:
                return True # has cycle
            v[i] = 1 # visiting
            for j in adj[i]:
                if j == parent:
                    continue
                if dfs(j, i):
                    return True
            v[i] = 2 # mark visited
            return False
        
        if dfs(0, -1):
            return False # has cycle
        
        for i in range(n):
            if v[i] != 2:
                return False # disconnected components
        
        return True