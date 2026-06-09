class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        h = []
        for ppl, _from, _to in trips:
            heapq.heappush(h, (_from, ppl))
            heapq.heappush(h, (_to, -ppl))
        
        passengers = 0
        while h:
            _, delta = heapq.heappop(h)
            passengers += delta
            if passengers > capacity:
                return False
        return True