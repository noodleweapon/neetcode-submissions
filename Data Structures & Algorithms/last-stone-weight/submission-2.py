import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) < 2:
            return max(stones) - min(stones)

        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            a, b = heapq.nlargest(2, stones)
            heapq.heappop(stones)
            heapq.heappop(stones)
            aa = -a
            bb = -b
            if aa > bb:
                heapq.heappush(bb - aa)
            
        return -stones[0]

