"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        newHeadDummy = Node(-1)
        newCurr = newHeadDummy
        d = {}
        while curr:
            newCurr.next = Node(curr.val)
            newCurr = newCurr.next
            d[curr] = newCurr
            curr = curr.next
        
        curr = head
        newCurr = newHeadDummy.next
        while curr:
            if curr.random:
                newCurr.random = d[curr.random]

            curr = curr.next
            newCurr = newCurr.next

        return newHeadDummy.next