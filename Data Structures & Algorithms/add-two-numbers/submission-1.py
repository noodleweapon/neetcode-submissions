# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        out = ListNode()
        head = out
        carry = 0

        while l1 or l2:
            n = carry
            if l1:
                n += l1.val
                l1 = l1.next
            if l2:
                n += l2.val
                l2 = l2.next
            
            carry = n // 10
            out.next = ListNode(n % 10)
            out = out.next
        
        if carry:
            out.next = ListNode(carry)
            
        return head.next

            # return 
            # 1,2,3,4 = 4321
            # 5,6 = 65
            # 4386 = 6,8,3,4


