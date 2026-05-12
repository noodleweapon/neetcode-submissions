# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        dp = defaultdict(list)
        l = 0
        r = 0
        def rec(node, x, y):
            nonlocal l, r
            l = min(l, x)
            r = max(r, x)
            if dp[x] and dp[x][-1][0] == y:
                dp[x][-1][1].append(node.val)
            else:
                dp[x].append((y, [node.val]))

            if node.left:
                rec(node.left, x - 1, y + 1)
            if node.right:
                rec(node.right, x + 1, y + 1)
        
        rec(root, 0, 0)
        res = []
        for i in range(l, r + 1):
            nn = []
            dp[i].sort(key=lambda x: x[0])
            for row in dp[i]:
                for item in row[1]:
                    nn.append(item)
            res.append(nn)
        return res

