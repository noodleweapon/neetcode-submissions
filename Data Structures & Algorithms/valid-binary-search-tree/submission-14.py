class Solution:
    def isValidBST(self, root):
        return self.valid(root, float('-inf'), float('inf'))

    def valid(self, node, low, high):
        if not node:
            return True
        if not (low < node.val < high):
            return False
        return self.valid(node.left, low, node.val) and self.valid(node.right, node.val, high)
