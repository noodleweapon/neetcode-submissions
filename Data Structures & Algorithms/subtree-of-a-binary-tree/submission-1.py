# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def isSame(self, root, subRoot):
        if not subRoot:
            return True
        if not root:
            return False

        if root.val != subRoot.val:
            return False
        if subRoot.left and not self.isSame(root.left, subRoot.left):
            return False
        if subRoot.right and not self.isSame(root.right, subRoot.right):
            return False
        return True

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False

        q = deque([root])
        while len(q) > 0:
            k = len(q)
            for _ in range(k):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
                if node.val != subRoot.val:
                    continue
                
                if not self.isSame(node, subRoot):
                    continue
                
                return True
        return False
                


