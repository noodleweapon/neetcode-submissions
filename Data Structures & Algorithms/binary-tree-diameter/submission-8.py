# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rec(self, arr, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        ld = self.rec(arr, root.left)
        rd = self.rec(arr, root.right)
        d = ld + rd
        return 1 + d

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        arr = []
        self.rec(arr, root)
        return max(arr)