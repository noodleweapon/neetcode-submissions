# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        visitedDepth = -1
        out = []

        def rec(node, depth):
            nonlocal visitedDepth
            nonlocal out
            if depth > visitedDepth:
                visitedDepth = depth
                out.append(node.val)
            
            if node.right:
                rec(node.right, depth + 1)
            if node.left:
                rec(node.left, depth + 1)
        rec(root, 0)

        return out


    def rightSideViewDfs(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = deque([root])
        out = []
        while q:
            out.append(q[-1].val)
            qLen = len(q)

            for i in range(qLen):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return out

#     def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
#         if not root:
#             return []
#         q = deque([root])
#         out = []
#         while q:
#             out.append(q[-1].val)
#             nodes = []
#             while q:
#                 nodes.append(q.popleft())
#             for node in nodes:
#                 if node.left:
#                     q.append(node.left)
#                 if node.right:
#                     q.append(node.right)
#         return out