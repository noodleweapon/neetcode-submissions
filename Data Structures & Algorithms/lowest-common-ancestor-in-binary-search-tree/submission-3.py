# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # try eulerian tour for fun, though we can just use the split property.
        p_ind = q_ind = -1
        tour = []
        def dfs(v, d):
            nonlocal p_ind, q_ind
            tour.append((v, d))
            if v.val == p.val:
                p_ind = len(tour) - 1
            if v.val == q.val:
                q_ind = len(tour) - 1

            if v.left:
                dfs(v.left, d + 1)
                tour.append((v, d))

            if v.right:
                dfs(v.right, d + 1)
                tour.append((v, d))

        dfs(root, 0)

        M = float("inf")
        u = None
        for i in range(min(p_ind, q_ind), max(p_ind, q_ind) + 1):
            v, d = tour[i]
            if d < M:
                M = d
                u = v
        return u





