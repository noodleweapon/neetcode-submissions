# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValid(root.left, root.val, -1) and self.isValid(root.right, root.val, 1)

    def isValid(self, root, parentVal, side):
        if not root:
            return True
        if side == -1:
            if root.val >= parentVal:
                return False
        else:
            if root.val <= parentVal:
                return False

        if root.left:
            if root.left.val >= root.val:
                return False
            newVal = root.val if side == 1 else parentVal
            if not self.isValid(root.left, newVal, -1):
                return False
        
        if root.right:
            if root.right.val <= root.val:
                return False
            newVal = root.val if side == -1 else parentVal
            if not self.isValid(root.right, newVal, 1):
                return False
        return True
        