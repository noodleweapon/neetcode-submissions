# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        q = deque([root])
        s = []
        while q:
            node = q.popleft()
            if not node:
                s.append(None)
                continue
            s.append(node.val)
            q.append(node.left)
            q.append(node.right)
        
        return ",".join(list(map(str, s)))
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "":
            return None

        def parse(x):
            if x == 'None':
                return None
            return TreeNode(int(x))

        s = deque(list(map(parse, data.split(","))))
        root = s.popleft()
        q = deque([root])
        while q:
            qLen = len(q)
            for i in range(qLen):
                node = q.popleft()
                if not node:
                    continue
                l = s.popleft()
                r = s.popleft()
                node.left = l
                node.right = r
                q.append(l)
                q.append(r)
        return root  