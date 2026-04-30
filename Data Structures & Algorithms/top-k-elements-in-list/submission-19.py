import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        for num in nums:
            heapq.heappush(heap, num)

        return heap[:k]