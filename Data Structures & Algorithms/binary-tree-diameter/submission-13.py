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
        ld = self.get_depth(root.left)
        rd = self.get_depth(root.right)
        d = ld + rd
        arr.append(d)
        if not root.left:
            self.rec(arr, root.left)
        if not root.right:
            self.rec(arr, root.right)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        arr = []
        self.rec(arr, root)
        return max(arr)

    def get_depth(self, root):
        if not root:
            return 0
        ld = self.get_depth(root.left)
        rd = self.get_depth(root.right)
        return 1 + max(ld, rd)

