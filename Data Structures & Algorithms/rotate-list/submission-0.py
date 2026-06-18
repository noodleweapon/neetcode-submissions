# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        
        n = 0
        cur = head
        last = None
        while cur:
            n += 1
            last = cur
            cur = cur.next
        
        print(n)
        
        k %= n

        if k == 0:
            return head
        
        k = n - k
        
        prv, cur = None, head
        for _ in range(k):
            prv, cur = cur, cur.next
        
        last.next, prv.next = head, None
        return cur
        
        [1,2,3,4,5,6]
        [2,3,4,5,6,1]


        [2,0,1]