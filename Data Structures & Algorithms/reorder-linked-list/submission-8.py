# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        stack = []
        cur = head
        while cur:
            stack.append(cur)
            cur = cur.next
        
        cur = head
        for _ in range(len(stack) // 2):
            nxt = cur.next
            top = stack.pop()
            cur.next = top
            top.next = nxt
            cur = nxt
        cur.next = None

        # 2,4,6,8

        # [0, 1, 2, 3, 4, 5]
        # [0, 1, 2, 3, 4, 5]

        # [0, 5, 1, 4, 2, 3]
        # [0, 1, 2]



