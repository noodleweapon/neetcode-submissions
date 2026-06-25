"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def findRoot(self, nodes: List['Node']) -> 'Node':
        seen = set()
        for node in nodes:
            for child in node.children:
                seen.add(child)
        for node in nodes:
            if node not in seen:
                return node
        
