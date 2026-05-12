"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        V = {}
        def dfs(v):
            if v in V:
                return V[v]
            V[v] = Node(v.val)
            for u in v.neighbors:
                V[v].neighbors.append(dfs(u))
            return V[v]
        return dfs(node)