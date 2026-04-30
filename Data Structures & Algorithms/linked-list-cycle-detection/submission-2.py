# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        fast = head
        slow = head

        while head.next and head.next.next:
            slow = head.next
            fast = head.next.next
            if slow.val == fast.val:
                return True


        return False