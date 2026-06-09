# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def delete(node):
            if not node:
                return None
            node.left = delete(node.left)
            node.right = delete(node.right)
            if node.left or node.right:
                return node
            if node.val != target:
                return node
            return None
        
        return delete(root)