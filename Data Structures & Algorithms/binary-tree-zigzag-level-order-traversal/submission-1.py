# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        level = [root]
        left_to_right = False
        res = []
        while level:
            left_to_right = not left_to_right
            new_level = []
            if left_to_right:
                res.append(list(map(lambda x: x.val, level)))
            else:
                res.append(list(reversed(list(map(lambda x: x.val, level)))))
            
            for i in range(len(level)):
                if level[i].left:
                    new_level.append(level[i].left)
                if level[i].right:
                    new_level.append(level[i].right)
            level = new_level
        return res