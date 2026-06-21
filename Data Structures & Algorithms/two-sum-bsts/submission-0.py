# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        if not root1 or not root2:
            return False
        
        q = deque([(root1, root2)])
        while q:
            a, b = q.popleft()
            tot = a.val + b.val
            if tot > target:
                if a.left:
                    q.append((a.left, b))
                if b.left:
                    q.append((a, b.left))

            elif tot < target:
                if a.right:
                    q.append((a.right, b))
                if b.right:
                    q.append((a, b.right))

            else:
                return True
        
        return False