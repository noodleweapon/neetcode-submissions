# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        def insert(node, val):
            if val < node.val:
                if not node.left:
                    node.left = TreeNode(val)
                else:
                    insert(node.left, val)
                # tmp = node.left
                # node.left = TreeNode(val)
                # if tmp.val < val:
                #     node.left.left = tmp
                # elif tmp.val > val:
                #     node.left.right = tmp
            elif val > node.val:
                if not node.right:
                    node.right = TreeNode(val)
                    return
                else:
                    insert(node.right, val)
                # tmp = node.right
                # node.right = TreeNode(val)
                # if tmp.val < val:
                #     node.right.left = tmp
                # elif tmp.val > val:
                #     node.right.right = tmp
        
        insert(root, val)
        return root