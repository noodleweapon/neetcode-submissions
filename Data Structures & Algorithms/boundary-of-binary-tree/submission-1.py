# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        def getL():
            stack = [root.val]
            if not root.left:
                return stack
            cur = root.left
            while cur:
                stack.append(cur.val)
                if cur.left:
                    cur = cur.left
                else:
                    cur = cur.right
            stack.pop()
            return stack
        
        def getR():
            stack = []
            if not root.right:
                return stack
            cur = root.right
            while cur:
                stack.append(cur.val)
                if cur.right:
                    cur = cur.right
                else:
                    cur = cur.left
            return list(reversed(stack))[1:]
        
        leaves = []
        def getLeaves(node):
            if node.left:
                getLeaves(node.left)
            if node.right:
                getLeaves(node.right)
            if not node.left and not node.right:
                if node != root:
                    leaves.append(node.val)

        getLeaves(root)

        return getL() + leaves + getR()