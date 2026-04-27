# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
import heapq

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        q = deque([root])
        h = []
        while q:
            qLen = len(q)
            for i in range(qLen):
                node = q.popleft()
                if not node:
                    continue
                heapq.heappush(h, node.val)
                q.append(node.left)
                q.append(node.right)
            
        return heapq.nsmallest(k, h)[-1]