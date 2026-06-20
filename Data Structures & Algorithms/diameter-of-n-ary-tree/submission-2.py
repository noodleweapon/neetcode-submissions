"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def diameter(self, root: 'Node') -> int:
        if not root:
            return 0
        res = 0

        def dfs(node):
            nonlocal res
            longest2 = []
            for child in node.children:
                l = 1 + dfs(child)
                longest2.append(l)
                longest2.sort(reverse=True)
                if len(longest2) > 2:
                    longest2.pop()
            if not longest2:
                return 0
            res = max(res, sum(longest2))
            return max(longest2)

        dfs(root)

        return res