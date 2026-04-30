# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        L = 0
        curr = head
        while curr and curr.next:
            curr = curr.next
            L += 1
        return L

        