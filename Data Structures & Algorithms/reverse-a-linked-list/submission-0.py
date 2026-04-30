# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p1 = head
        p2 = head.next
        while p2 != None:
            p1.next = None
            p2next = p2.next
            p2.next = p1

            p1 = p2
            p2 = p2next
        return p2
