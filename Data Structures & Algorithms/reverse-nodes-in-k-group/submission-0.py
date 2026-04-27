# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur = head
        laggingHead = ListNode(-1)
        lagging = laggingHead
        s = []
        while cur:
            s.append(cur)
            cur = cur.next
            if len(s) != k:
                continue
            print('stack has k items')
            while len(s) > 0:
                node = s.pop()
                node.next = None
                lagging.next = node
                lagging = lagging.next
            lagging.next = cur

        return laggingHead.next