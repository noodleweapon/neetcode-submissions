# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        M = 1
        def dfs(node): # --> longest seq starting from that (inclusive)
            nonlocal M
            L = 1
            if node.left:
                P = dfs(node.left)
                if node.left.val == node.val + 1:
                    L = max(L, P + 1)
                    M = max(M, L)

            if node.right:
                P = dfs(node.right)
                if node.right.val == node.val + 1:
                    L = max(L, P + 1)
                    M = max(M, L)
            return L

        dfs(root)
        return M
