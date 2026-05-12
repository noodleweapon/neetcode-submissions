# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, node, m):
        if not node:
            return
        count = 0
        if node.val >= m:
            m = node.val
            count += 1
        if node.left:
            count += self.dfs(node.left, m)
        if node.right:
            count += self.dfs(node.right, m)
        return count

    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        return self.dfs(root, root.val)
        