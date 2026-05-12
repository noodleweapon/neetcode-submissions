# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        dummy = ListNode()
        dummy.next = head
        curr = head
        prv = dummy
        s = []
        while curr:
            s.append(curr)
            nxt = curr.next
            if len(s) % k == 0:
                while s:
                    node = s.pop()
                    node.next = None ### this
                    prv.next = node
                    prv = node

            curr = nxt
        
        for node in s:
            prv.next = node
            prv = node
        
        return dummy.next