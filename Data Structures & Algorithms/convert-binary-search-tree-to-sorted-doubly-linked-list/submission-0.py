"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        def toDD(node): # --> [left, right]
            l, r = node, node
            if node.left:
                L = toDD(node.left)
                l.left, L[1].right = L[1], l
                l = L[0]
            if node.right:
                R = toDD(node.right)
                r.right, R[0].left = R[0], r
                r = R[1]
            return [l, r]
        
        l, r = toDD(root)
        l.left, r.right = r, l
        return l