class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        heap = list(set(nums))
        heapq.heapify(heap)

        consec = 1
        prev = heap.heappop()
        while len(heap) > 0:
            curr = heap.heappop()
            if curr - prev != 1:
                consec = 1
                prev = curr
        return consec

