# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rec(self, node, s, l):
        if not node:
            return True
        if node.val < s or node.val > l:
            return False
        
        left_ok = self.rec(node.left, s, node.val - 1)
        right_ok = self.rec(node.right, node.val + 1, l)
        return left_ok and right_ok

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.rec(root, float("-inf"), float("inf"))