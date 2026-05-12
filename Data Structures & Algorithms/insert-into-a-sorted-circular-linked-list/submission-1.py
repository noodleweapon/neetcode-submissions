# Definition for a Node.
# class Node:
#   def __init__(self, val=None, next=None):
#        self.val = val
#        self.next = next

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        node = Node(insertVal)
        if not head:
            node.next = node
            return node
        
        first = True
        prev = head
        curr = head.next

        while first or prev != head:
            first = False
            ok = False
            if prev.val <= curr.val:
                if prev.val <= insertVal <= curr.val:
                    ok = True
            else:
                if prev.val <= insertVal:
                    ok = True
                elif insertVal <= curr.val:
                    ok = True

            if ok:
                prev.next = node
                node.next = curr
                return head
            
            prev = curr
            curr = curr.next
        
        prev.next = node
        node.next = curr
        return head
        
        # insert if prev <= val <= curr
        # if curr < prev: curr = INF
        # if prev > curr: prev = -INF

        # Now what if trying to insert 5, but all 3s.
        # Then infinite loop. So then after reached prev = head,
        # should insert there.
