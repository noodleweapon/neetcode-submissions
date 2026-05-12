class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []
        for num in nums:
            heapq.heappush(h, num)
            if len(h) > k:
                heapq.heappop(h)
        return heapq.heappop(h)

        # h = [-v for v in nums]
        # heapq.heapify(h)
        # return -heapq.nsmallest(k, h)[-1]