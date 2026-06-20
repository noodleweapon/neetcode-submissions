# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head

        cur = dummy
        while cur:
            if cur.val != 9:
                last_non_9 = cur
            cur = cur.next
        
        last_non_9.val += 1
        cur = last_non_9.next
        while cur:
            cur.val = 0
            cur = cur.next

        if dummy.val == 0:
            return dummy.next
        else:
            return dummy