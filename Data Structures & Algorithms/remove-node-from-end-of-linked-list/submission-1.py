# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
            
        curr = head
        ind = 0

        a = head
        b = head

        while curr:
            if ind > n:
                a = a.next
            if ind > n - 1:
                b = b.next
            ind += 1
            curr = curr.next

        if a == b:
            return b.next
        else:
            a.next = b.next
            return head

