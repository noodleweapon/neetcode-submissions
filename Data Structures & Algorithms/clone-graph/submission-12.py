"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, first_node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        d = {} # real --> clone
        def clone_dfs(node):
            if node.val in d:
                return d[node.val]
            cloned_node = Node(node.val)
            d[node.val] = cloned_node
            for neighbor in node.neighbors:
                cloned_neighbor = clone_dfs(neighbor)
                # cloned_node.neighbors.append(cloned_neighbor) # << I had to remove this because original graph already has its own reverse edges.
                cloned_neighbor.neighbors.append(cloned_node)
            return cloned_node

        return clone_dfs(first_node)