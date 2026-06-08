# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        prv, cur = dummy, head
        
        stack = []
        while cur:
            nxt = cur.next
            stack.append(cur)
            if len(stack) == k:
                while stack:
                    node = stack.pop()
                    node.next = None
                    prv.next = node
                    prv = node
            cur = nxt

        for elem in stack:
            prv.next = elem
            prv = elem

        return dummy.next


        # dummy,1,2,3,4,5
        # dummy,3,2,1,4,