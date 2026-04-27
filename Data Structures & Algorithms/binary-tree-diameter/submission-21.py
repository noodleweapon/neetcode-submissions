# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rec(self, arr, root: Optional[TreeNode]) -> int:
        if not root:
            return
        ld = self.get_depth(root.left)
        rd = self.get_depth(root.right)
        d = ld + rd
        arr.append(d)
        if root.left:
            self.rec(arr, root.left)
        if root.right:
            self.rec(arr, root.right)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        stack = [root]
        mp = {}

        while stack:
            node = stack[-1]

            if node.left and node.left not in mp:
                stack.append(node.left)
            elif node.right and node.right not in mp:
                stack.append(node.right)
            else:
                stack.pop()

                leftHeight, leftDiameter = mp[node.left] if node.left else [0, 0]
                rightHeight, rightDiameter = mp[node.right] if node.right else [0, 0]

                maxh_at_node = 1 + max(leftHeight, rightHeight)
                max_diameter_at_node = max(leftHeight + rightHeight, leftDiameter, rightDiameter)

                mp[node] = (maxh_at_node, max_diameter_at_node)

        return mp[root][1]


    def old(self, root):
        arr = []
        self.rec(arr, root)
        if len(arr) == 0:
            return 0
        return max(arr)

    def get_depth(self, root):
        if not root:
            return 0
        ld = self.get_depth(root.left)
        rd = self.get_depth(root.right)
        return 1 + max(ld, rd)

