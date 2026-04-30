# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        M = float("-inf")
        dp = {}
        def maxIncluding(node):
            if not node:
                return 0
            if node.val in dp:
                return dp[node.val]
            L = maxIncluding(node.left)
            R = maxIncluding(node.right)
            res = max([L, R, 0]) + node.val
            dp[node.val] = res
            return res

        def rec(node):
            nonlocal M, maxIncluding
            if not node:
                return
            L = max(0, maxIncluding(node.left))
            R = max(0, maxIncluding(node.right))
            S = L + R + node.val
            M = max(M, S)
            rec(node.left)
            rec(node.right)
        
        rec(root)
        return M
