class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        g = [set() for _ in range(n)]
        for a, b in edges:
            g[a].add(b)
            g[b].add(a)
        
        leaves = [i for i in range(n) if len(g[i]) == 1]
        nodes = n
        
        while nodes > 2:
            new_leaves = []
            nodes -= len(leaves)
            
            for u in leaves:
                v = g[u].pop() # since it only has one neighbor.
                g[v].remove(u)
                if len(g[v]) == 1:
                    new_leaves.append(v)
            
            leaves = new_leaves
        
        return leaves