# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def delete(node, v):
            if not node:
                return None
            if node.val < v:
                node.right = delete(node.right, v)
                return node
            if node.val > v:
                node.left = delete(node.left, v)
                return node
            if node.left == None:
                return node.right
            if node.right == None:
                return node.left

            cur = node.left
            while cur.right:
                cur = cur.right
            node.val = cur.val
            node.left = delete(node.left, node.val)
            return node
        
        return delete(root, key)
