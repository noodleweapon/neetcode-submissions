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
        l = r = 0
        q = deque([(root, 0)])
        d = defaultdict(list)
        while q:
            (node, x) = q.popleft()
            d[x].append(node.val)
            l = min(l, x)
            r = max(r, x)
            if node.left:
                q.append((node.left, x - 1))
            if node.right:
                q.append((node.right, x + 1))

        return [d[i] for i in range(l, r + 1)]