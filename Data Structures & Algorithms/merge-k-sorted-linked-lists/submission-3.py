# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    
    def mergeKLists(self, ls: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = ListNode(None)
        curr = head
        h = []
        for i, l in enumerate(ls):
            if l:
                heapq.heappush(h, (l.val, i, l))

        while h:
            v, i, node = heapq.heappop(h)
            l = ls[i]
            if l:
                heapq.heappush(h, (l.val, i, l))
                ls[i] = l.next
            curr.next = node
            curr = curr.next
        
        return head.next


    def mergeKListsNoHeap(self, ls: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = ListNode(None)
        curr = head

        while curr:
            ind = None
            for i, l in enumerate(ls):
                if not l:
                    continue
                if (ind != None) and ls[ind].val <= l.val:
                    continue
                ind = i
            if ind == None:
                break
            curr.next = ls[ind]
            ls[ind] = ls[ind].next
            curr = curr.next

        return head.next