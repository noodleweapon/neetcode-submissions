# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        # assume can go 1-2-1
        M = 1
        def dfs(node): # returns longest seq starting from that node.
            nonlocal M
            left = 0
            right = 0
            if node.left:
                if abs(node.left.val - node.val) == 1:
                    left = dfs(node.left)
                else:
                    dfs(node.left)
            
            if node.right:
                if abs(node.right.val - node.val) == 1:
                    right = dfs(node.right)
                else:
                    dfs(node.right)

            
            M = max(M, left + right + 1)
            return max(left, right) + 1
        
        dfs(root)
        return M