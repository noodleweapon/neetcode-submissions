# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def getLastTwo(self, curr):
        c = curr
        while c and c.next:
            if not c.next.next:
                break
            c = c.next
        return [c, c.next]

    def reorderList(self, head: Optional[ListNode]) -> None:
        L = 0
        curr = head
        while curr:
            curr = curr.next
            L += 1

        start = head
        N = L//2
        if L % 2 == 0:
            N -= 1
        for i in range(N):
            # print(i)
            # a, b = self.getLastTwo(start)
            # print(a.val, b.val)
            # continue
            a, b = self.getLastTwo(head)
            b.next = start.next
            a.next = None
            start.next = b
            start = start.next.next


