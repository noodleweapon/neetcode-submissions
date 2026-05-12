# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        out = 0
        def depth(node):
            nonlocal out
            if not node:
                return 0
            l = depth(node.left)
            r = depth(node.right)
            new_res = 1 + max(l, r)
            out = max(l + r, out)
            return new_res
            
        depth(root)
        return out