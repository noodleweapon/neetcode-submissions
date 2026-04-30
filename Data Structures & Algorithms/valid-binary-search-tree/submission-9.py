# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.isValid(root, None)

    def isValid(self, root, parentVal):
        if root.left:
            if root.left.val >= root.val:
                return False
            if parentVal != None and root.left.val > parentVal:
                return False
            if not self.isValid(root.left, root.val):
                return False
        
        if root.right:
            if root.right.val <= root.val:
                return False
            if parentVal != None and root.right.val < parentVal:
                return False
            if not self.isValid(root.right, root.val):
                return False
        return True
        