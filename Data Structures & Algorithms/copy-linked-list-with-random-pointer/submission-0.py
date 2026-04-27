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
        if not head:
            return None

        _head = Node(-1)
        _curr = _head
        curr = head

        d = {}

        while curr:
            _curr.next = Node(curr.val)
            _curr = _curr.next
            d[curr] = _curr
            curr = curr.next

        _curr = _head.next
        curr = head
        while curr:
            if curr.random:
                _curr.random = d[curr.random]
            _curr = _curr.next
            curr = curr.next
        
        return _head.next

