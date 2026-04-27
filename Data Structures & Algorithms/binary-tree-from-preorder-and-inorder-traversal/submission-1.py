# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        pos = {v: i for i, v in enumerate(inorder)}
        pre_idx = 0

        def build(l, r):
            nonlocal preorder, inorder, pre_idx
            val = preorder[pre_idx]
            ind = pos[val] # inorder.index(val)
            node = TreeNode(val)
            pre_idx += 1

            if ind > l:
                # val_l = preorder[ind - 1]
                node.left = build(l, ind - 1)

            if ind < r:
                # val_r = preorder[ind + 1]
                node.right = build(ind + 1, r)
            
            return node

        return build(0, len(preorder) - 1)
