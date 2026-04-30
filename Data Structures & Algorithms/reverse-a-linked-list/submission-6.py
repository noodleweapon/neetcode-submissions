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
        while p2.next != None:
            nextP1 = p1.next
            nextP2 = p2.next

            p2.next = p1
            p2.next = nextP2
            p1.next = nextP1

        head.next = None
        return p2
