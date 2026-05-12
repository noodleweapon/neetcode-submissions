# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, node, res, k):
        if not node:
            return
        if len(res) >= k:
            return
        self.dfs(node.left, res, k)
        if len(res) < k:
            res.append(node)
        self.dfs(node.right, res, k)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        self.dfs(root, res, k)
        print(len(res))
        return res[-1].val
