# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        h = []
        dummy = ListNode()
        cur = dummy

        for l in range(len(lists)):
            if lists[l]:
                heapq.heappush(h, (lists[l].val, l))
        
        while h:
            val, l = heapq.heappop(h)
            nxt = lists[l].next
            lists[l].next = None
            cur.next = lists[l]
            cur = cur.next
            if nxt:
                lists[l] = nxt
                heapq.heappush(h, (lists[l].val, l))
        
        return dummy.next

            
            

        # [1,2,4]
        # [1,3,5]
        # [3,6]