# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        head = None
        def dfs(node):
            nonlocal head
            if node.left:
                dfs(node.left)
                l, r = node.left, node.right
                l.left, l.right = r, node
                node.left, node.right = None, None

            if not head:
                head = node
        dfs(root)
        return head