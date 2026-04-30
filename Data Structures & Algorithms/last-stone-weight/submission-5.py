import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) < 2:
            return max(stones) - min(stones)

        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            a, b = heapq.nsmallest(2, stones)
            heapq.heappop(stones)
            heapq.heappop(stones)
            aa = -a
            bb = -b
            if aa > bb:
                heapq.heappush(heap, bb - aa)
        
        if not stones:
            return 0
        return -stones[0]

