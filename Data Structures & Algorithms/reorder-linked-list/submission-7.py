# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        stack = []
        curr = head
        while curr:
            stack.append(curr)
            curr = curr.next

        curr = head
        N = len(stack)
        for i in range(N // 2):
            temp = curr.next
            curr.next = stack.pop()
            curr.next.next = temp
            curr = temp
        curr.next = None # i missed this