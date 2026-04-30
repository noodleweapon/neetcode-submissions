class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        heap = list(set(nums))
        heapq.heapify(heap)
        if len(heap) < 2:
            return len(heap)

        consec = 0
        max_consec = 1
        prev = heapq.heappop(heap)
        while len(heap) > 0:
            curr = heapq.heappop(heap)
            consec += 1
            if consec > max_consec:
                max_consec = consec
            
            if curr - prev != 1:
                consec = 0
            prev = curr
        return max_consec

