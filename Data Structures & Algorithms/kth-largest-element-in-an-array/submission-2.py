class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = [-v for v in nums]
        heapq.heapify(h)
        return -heapq.nsmallest(k, h)[-1]