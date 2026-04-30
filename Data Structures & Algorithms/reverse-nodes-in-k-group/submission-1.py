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
            if len(s) == k:
                while s:
                    node = s.pop()
                    node.next = None
                    lag.next = node
                    lag = lag.next

                lag.next = curr.next
            curr = curr.next

        # if s:
        #     lag.next = s[-1]

        return lagHead.next