# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isSame(node, subRoot):
            if not node:
                return not subRoot
            if not subRoot:
                return not node
            if node.val != subRoot.val:
                return False
            if not isSame(node.left, subRoot.left):
                return False
            if not isSame(node.right, subRoot.right):
                return False
            return True

        q = [root]
        while q:
            node = q.pop()
            if isSame(node, subRoot):
                return True
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            
        return False