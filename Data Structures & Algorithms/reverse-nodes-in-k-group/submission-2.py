# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        lagHead = ListNode(-1)
        lag = lagHead
        s = []
        while curr:
            s.append(curr)
            nxt = curr.next
            if len(s) == k:
                while s:
                    node = s.pop()
                    node.next = None
                    lag.next = node
                    lag = node

                # lag.next = curr.next
            curr = nxt

        for elem in s:
            lag.next = elem
            lag = lag.next

        return lagHead.next