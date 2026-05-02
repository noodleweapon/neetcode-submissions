class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        h = []
        for p, a, b in trips:
            heapq.heappush(h, (a, p))
            heapq.heappush(h, (b, -p)) # will run first which is good.
        
        x = 0
        while h:
            (_, delta) = heapq.heappop(h)
            x += delta
            if x > capacity:
                return False
        return True