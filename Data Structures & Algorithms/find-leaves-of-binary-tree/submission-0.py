# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        count = defaultdict(int)
        leaves = deque([])
        parent = {}
        def dfs(node):
            if not node.left and not node.right:
                leaves.append(node)
                return
            if node.left:
                count[node] += 1
                dfs(node.left)
                parent[node.left] = node
            if node.right:
                count[node] += 1
                dfs(node.right)
                parent[node.right] = node
        
        if dfs(root):
            return [[root.val]]
        res = []
        while leaves:
            res.append([])
            for _ in range(len(leaves)):
                node = leaves.popleft()
                res[-1].append(node.val)
                if node not in parent:
                    continue
                p = parent[node]
                count[p] -= 1
                if count[p] != 0:
                    continue
                leaves.append(p)

        return res