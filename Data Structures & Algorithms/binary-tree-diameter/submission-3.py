# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rec(self, arr, root: Optional[TreeNode]) -> int:
        ld = self.rec(root.left)
        rd = self.rec(root.right)
        d = ld + rd

    def diameterOfBinaryTree(self, arr, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        arr = []
        self.rec(arr, root)
        return max(arr)