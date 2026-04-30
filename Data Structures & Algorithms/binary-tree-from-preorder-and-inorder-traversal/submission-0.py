# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], _inorder: List[int]) -> Optional[TreeNode]:
        d = {}
        def build(root_val, inorder):
            nonlocal preorder
            root_ind = inorder.index(root_val)
            to_left = inorder[:root_ind]
            to_right = inorder[root_ind+1:]

            root = TreeNode(root_val)

            if root_ind > 0:
                left_val = inorder[root_ind - 1]
                root.left = build(left_val, to_left)
            
            if root_ind < len(inorder) - 1:
                right_val = inorder[root_ind + 1]
                root.right = build(right_val, to_right)
            
            return root

        the_root = build(preorder[0], _inorder)
        return the_root
