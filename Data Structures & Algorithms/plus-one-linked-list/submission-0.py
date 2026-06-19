# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        stack = []
        cur = head
        while cur:
            stack.append(cur)
            cur = cur.next
        if not stack:
            return ListNode(1)
        stack[-1].val += 1
        while stack and stack[-1].val >= 10:
            node = stack.pop()
            node.val -= 10
            if stack:
                stack[-1].val += 1
            else:
                new_head = ListNode(1)
                new_head.next = node
                return new_head
        return head