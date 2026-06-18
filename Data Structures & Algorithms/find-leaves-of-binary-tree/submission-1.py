# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        levels = []
        def dfs(node):
            if not node:
                return 0
            leftH = dfs(node.left)
            rightH = dfs(node.right)
            H = 1 + max(leftH, rightH)
            while len(levels) < H:
                levels.append([])
            levels[H - 1].append(node.val)
            return H
        dfs(root)
        return levels