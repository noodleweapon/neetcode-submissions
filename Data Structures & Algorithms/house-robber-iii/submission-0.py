# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def profit(node): # --> (including, excluding itself)
            if not node:
                return (0, 0)
            if not node.left and not node.right:
                return (node.val, 0)
            
            left = profit(node.left)
            right = profit(node.right)
            excluding_node = left[0] + right[0]
            including_node = left[1] + right[1] + node.val
            return (max(including_node, excluding_node), excluding_node)
        
        return profit(root)[0]
