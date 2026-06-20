# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import sys

sys.setrecursionlimit(100000)

class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        nodes = []
        def dfs(node):
            if node.left:
                dfs(node.left)
            nodes.append(node)
            if node.right:
                dfs(node.right)
        dfs(root)
        add = 0
        for i in reversed(range(len(nodes))):
            node = nodes[i]
            add += node.val
            node.val += add - node.val
        
        return root    

        # def dfs(node, accum):
        #     if node.right:
        #         accum += node.right.val
        #         accum += dfs(node.right, accum)
        #     node.val += accum
        #     if node.left:
        #         dfs(node.left, accum)
        #     return accum

        # dfs(root, 0)
        # return root

        # 10,
        # 9,15,
        # 4,null,12,19,
        # 2,5,    11