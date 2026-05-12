# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        out = 0
        def rec(node, M):
            nonlocal out
            if node.val >= M:
                out += 1
            M = max(node.val, M)
            if node.left:
                rec(node.left, M)
            if node.right:
                rec(node.right, M)

        rec(root, root.val)
        return out