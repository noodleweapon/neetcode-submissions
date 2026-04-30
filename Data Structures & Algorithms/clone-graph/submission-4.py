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
            V[v.val] = Node(v.val)
            for u in v.neighbors:
                if u.val in V:
                    continue
                u_clone = dfs(u)
                u_clone.neighbors.append(V[v.val])
                V[v.val].neighbors.append(u_clone)
            return V[v.val]
        return dfs(node)