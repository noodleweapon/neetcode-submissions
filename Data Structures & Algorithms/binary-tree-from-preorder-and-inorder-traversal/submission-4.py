# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        pre = 0
        def build(l, r):
            nonlocal pre
            if l > r:
                return None
            val = preorder[pre]
            pre += 1
            m = inorder.index(val)
            node = TreeNode(val)
            node.left = build(l, m - 1)
            node.right = build(m + 1, r)
            return node
        
        return build(0, len(preorder) - 1)
        
        [1,2,3,4]
        [2,1,3,4]