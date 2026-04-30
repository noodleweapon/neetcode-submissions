# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        if head.next == None:
            return head

        p1 = head
        p2 = head.next
        while True:
            p2next = p2.next
            p2.next = p1

            p1 = p2
            p2 = p2next
            if p2 == None:
                head.next = None
                return p2

