"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        s = {node.val}
        originalCopy = Node(node.val)
        q = deque([(node, originalCopy)])
        created = {}
        while q:
            for i in range(len(q)):
                curr = q.popleft()
                for n in curr[0].neighbors:
                    if n.val in s:
                        continue
                    
                    nCopy = None
                    if n.val in created:
                        nCopy = created[n.val]
                        if curr[1] not in nCopy.neighbors:
                            nCopy.neighbors.append(curr[1])
                    else:
                        nCopy = Node(n.val, [curr[1]])
                        created[n.val] = nCopy
                    
                    curr[1].neighbors.append(nCopy)
                    s.add(n.val)
                    q.append((n, nCopy))
        return originalCopy




