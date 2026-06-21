# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        res = 0
        def uni(node): # T/F
            nonlocal res
            if not node:
                return True
            
            L = uni(node.left)
            R = uni(node.right) # MISTAKE: EARLY RETURN BLOCKS RIGHT TREE.
            if not L or (node.left and node.left.val != node.val):
                return False
            if not R or (node.right and node.right.val != node.val):
                return False
            res += 1
            return True
            
        if root:
            uni(root)
        return res