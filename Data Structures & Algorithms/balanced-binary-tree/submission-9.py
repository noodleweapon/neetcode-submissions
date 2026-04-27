# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getDepth(self, node):
        if not node:
            return 0
        return 1 + max(self.getDepth(node.left), self.getDepth(node.right))

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        L = self.getDepth(root.left)
        R = self.getDepth(root.right)
        if abs(L - R) > 1:
            return False

        if root.left:
            if not self.isBalanced(root.left):
                return False

        if root.right:
            if not self.isBalanced(root.right):
                return False
        
        return True