"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        def clone(node):
            if not node:
                return None
            clone_node = Node(node.val)
            for child in node.children:
                clone_node.children.append(clone(child))
            return clone_node

        return clone(root)