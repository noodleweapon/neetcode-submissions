# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sol(self, node, p, q):
        if node.val == p.val or node.val == q.val:
            return node
        if not node.left:
            return self.sol(node.right, p, q)
        if not node.right:
            return self.sol(node.left, p, q)

        if p.val < node.val and q.val < node.val:
            return self.sol(node.left, p, q)
        if p.val > node.val and q.val > node.val:
            return self.sol(node.right, p, q)
        return node

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        return self.sol(root, p, q)