# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        M = float("-inf")
        def rec(node):
            nonlocal M
            if not node:
                return 0
            

            l = rec(node.left)
            r = rec(node.right)
            score = max(l, 0) + max(r, 0) + node.val
            M = max(M, score)
            return node.val + max(l, r, 0)
        
        rec(root)
        return M

    def maxPathSumOld(self, root: Optional[TreeNode]) -> int:
        M = float("-inf")
        dp = {}
        def maxIncluding(node):
            if not node:
                return 0
            if node in dp:
                return dp[node]
            L = maxIncluding(node.left)
            R = maxIncluding(node.right)
            res = max([L, R, 0]) + node.val
            dp[node] = res
            return res

        def rec(node):
            nonlocal M, maxIncluding
            if not node:
                return
            L = max(0, maxIncluding(node.left))
            R = max(0, maxIncluding(node.right))
            M = max(L + R + node.val, M)
            rec(node.left)
            rec(node.right)
        
        rec(root)
        return M


#          5,
#        4, 8,
#     11,null, 13,     4,
# 7,2,    null,null,  null,1
# 13 + 8 + 5 + 4 + 11 + 7 = 48