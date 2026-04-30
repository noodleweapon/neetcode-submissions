# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        if list2 == None:
            return list1

        bigger = None
        smaller = None
        if list1.val > list2.val:
            bigger = list1
            smaller = list2
        else:
            bigger = list2
            smaller = list1
        
        head = ListNode(-1)
        curr = head

        while smaller.next != None or bigger.next != None:
            while smaller.val <= bigger.val:
                curr.next = smaller
                smaller = smaller.next

            temp = bigger
            bigger = smaller
            smaller = temp

        return head.next