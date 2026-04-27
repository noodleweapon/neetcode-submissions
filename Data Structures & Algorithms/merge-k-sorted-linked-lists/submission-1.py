# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = ListNode(-1)
        curr = head
        k = len(lists)

        while lists:
            mi = 0
            mv = lists[0]
            for i in range(len(lists) - 1, -1, -1):
                lv = lists[i]
                if lv.val < mv.val:
                    mv = lv
                    mi = i
            
            curr.next = lists[mi]
            curr = curr.next
            lists[mi] = lists[mi].next

            if None in lists:
                lists.remove(None)


        return head.next