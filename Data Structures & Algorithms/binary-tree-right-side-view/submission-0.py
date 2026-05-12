# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = deque([root])
        arr = []
        while q:
            l = len(q)
            row = []
            for _ in range(l):
                top = q.popleft()
                row.append(top.val)
                if top.left:
                    q.append(top.left)
                if top.right:
                    q.append(top.right)
            arr.append(row)
        
        res = [row[-1] for row in arr]
        return res
