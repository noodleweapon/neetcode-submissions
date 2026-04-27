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
            qLen = len(q)
            for i in range(qLen):
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
        
        print(data)

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

            


        # q = deque(s)
        # n = 1
        # root = q[0]
        # while q and n:
        #     new_n = 0
        #     for i in range(n):
        #         node = q.popleft()
        #         if not node:
        #             continue
        #         offset = (n - i - 1) + (i * 2)
        #         node.left = q[offset]
        #         node.right = q[offset + 1]
        #         new_n += 1

        #     n = new_n
        return root
