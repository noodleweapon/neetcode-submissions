# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        M = float("-inf")
        def maxpath(node):
            nonlocal M
            if not node:
                return 0
            L = maxpath(node.left)
            R = maxpath(node.right)
            M = max(M, max(0, L) + max(0, R) + node.val)
            return max([L, R, 0]) + node.val

        maxpath(root)
        return M