# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def depth(self, root, dp, res):
        if not root:
            return 0
        if root in dp:
            return dp[root]
        l = self.depth(root.left, dp, res)
        r = self.depth(root.right, dp, res)
        new_res = 1 + max(l, r)
        dp[root] = new_res
        res[0] = max(l + r, res[0])
        return new_res

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        dp = {}
        res = [0]
        self.depth(root, dp, res)
        return res[0]