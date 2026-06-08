# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        cur = dummy.next
        prv = dummy
        ind = 0
        outer_left = inner_left = None
        outer_right = inner_right = None

        while cur:
            ind += 1
            if ind == left:
                outer_left, inner_left = prv, cur
            if ind == right:
                inner_right, outer_right = cur, cur.next
            prv, cur = cur, cur.next

        prv = inner_left
        cur = inner_left.next
        while cur and cur != outer_right:
            nxt = cur.next
            cur.next = prv
            prv, cur = cur, nxt
        
        outer_left.next = inner_right
        inner_left.next = outer_right
        return dummy.next

        # head=[1-->2-->3]
        # [1-->3, 2<--3]
        # left=2
        # right=3

        # [1-->4, 2<--3<--4. 2-->5]

        # 1-->[2-->3-->4]-->5
        # 1-->4, [2<--3<--4] 2-->5
        # 1,4,3,2,5