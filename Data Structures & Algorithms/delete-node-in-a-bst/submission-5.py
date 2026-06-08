# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def delete(node):
            if not node:
                return None
            if key < node.val:
                node.left = delete(node.left)
                return node
            if key > node.val:
                node.right = delete(node.right)
                return node
            if not node.right:
                return node.left
            if not node.left:
                return node.right
            original_left = node.left
            original_right = node.right
            if not original_right.left:
                node = original_right
                node.left = original_left
                return node

            curr, parent = original_right.left, original_right
            while curr and curr.left:
                curr, parent = curr.left, curr
            
            parent.left = curr.right # I had None here, which was wrong.
            curr.left = original_left
            curr.right = original_right
            return curr
        
        return delete(root)