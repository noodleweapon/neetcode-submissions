# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        dp = {None: [0, 0]}
        stack = [root]
        while len(stack) > 0:
            node = stack[-1]
            if node.left != None and node.left not in dp:
                stack.append(node.left)
            elif node.right != None and node.right not in dp:
                stack.append(node.right)
            else:
                stack.pop()
                lh = max(dp[node.left])
                rh = max(dp[node.right])
                diff = abs(lh - rh)
                if diff > 1:
                    return False
                dp[node] = (lh, rh)
        
        return True