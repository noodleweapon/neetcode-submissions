# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getPath(self, root: TreeNode, p: TreeNode, pPath):
        if not root:
            return False
        pPath.append(root)
        if root.val == p.val:
            return True
        if self.getPath(root.left, p, pPath):
            return True
        if self.getPath(root.right, p, pPath):
            return True
        pPath.pop()
        return False

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        pPath = []
        if not self.getPath(root, p, pPath):
            return None
        qPath = []
        if not self.getPath(root, q, qPath):
            return None
        
        ances = root
        while pPath and qPath and (pPath[0] == qPath[0]):
            ances = pPath.pop(0)
            qPath.pop(0)
            print('pop')
        
        return ances
