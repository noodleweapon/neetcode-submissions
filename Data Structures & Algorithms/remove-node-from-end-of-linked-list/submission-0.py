# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        L = 0
        curr = head
        while curr:
            L += 1
            curr = curr.next
        
        if n == L:
            return head.next

        curr = head
        for _ in range(L - n - 1):
            curr = curr.next
        curr.next = None if not curr.next else curr.next.next
        return head