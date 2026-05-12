class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        g = [set() for _ in range(n)]
        for a, b in edges:
            g[a].add(b)
            g[b].add(a)
        
        nodes = set([i for i in range(n)])
        def find_leaves():
            return [i for i in range(n) if len(g[i]) == 1]
        
        while nodes:
            if len(nodes) <= 2:
                return list(nodes)
            
            leaves = find_leaves()
            
            for u in leaves:
                nodes.remove(u)
                for v in g[u]:
                    g[v].remove(u)
                g[u] = set()