class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = [-v for v in stones]
        heapq.heapify(h)
        while len(h) >= 2:
            x = -heapq.heappop(h)
            y = -heapq.heappop(h)
            if x < y:
                heapq.heappush(h, x - y)
            elif x > y:
                heapq.heappush(h, y - x)
        
        if len(h) == 0:
            return 0
        return -heapq.heappop(h)